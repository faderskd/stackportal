from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


class Category(models.Model):
    """
    Kategoria tematyczna
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = _("categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return _('%s' % self.name)


class Question(models.Model):
    """
    Pytanie
    """
    title = models.CharField(max_length=300, unique=True, verbose_name=_("question"))
    content = models.TextField(verbose_name=_("content"))
    category = models.ForeignKey(Category, related_name='questions', verbose_name=_("category"), default=1)
    user = models.ForeignKey(User, related_name='questions', verbose_name=_("user"))
    set_date = models.DateTimeField(auto_now_add=True, verbose_name=_("set date"))
    last_activity = models.DateTimeField(auto_now=True, verbose_name=_("last activity"))
    solved = models.BooleanField(default=False, verbose_name=_("solved"))
    views = models.PositiveIntegerField(default=0, verbose_name=_("views"))
    likes = models.PositiveIntegerField(default=0, verbose_name=_("likes"))
    dislikes = models.PositiveIntegerField(default=0, verbose_name=_("dislikes"))
    favorites = models.PositiveIntegerField(default=0, verbose_name=_("favorites"))
    last_modified_by = models.ForeignKey(User, null=True, related_name='questions_modified', verbose_name=_("last_modified_by"))

    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return self.likes - self.dislikes

    def __str__(self):
        return _('%s' % self.title)


class Answer(models.Model):
    """
    Odpowiedź do pytania, user nie może odpowiadać więcej niż raz na dane pytanie
    może tylko edytować
    """
    content = models.TextField()
    question = models.ForeignKey(Question, blank=True, null=True, related_name='answers', verbose_name=_("content"))
    user = models.ForeignKey(User, related_name='answers', verbose_name=_("user"))
    set_date = models.DateTimeField(auto_now_add=True, verbose_name=_("set date"))
    last_activity = models.DateTimeField(auto_now=True, verbose_name=_("last activity"))
    likes = models.PositiveIntegerField(default=0, verbose_name=_("likes"))
    dislikes = models.PositiveIntegerField(default=0, verbose_name=_("dislikes"))
    solved = models.BooleanField(default=False, verbose_name=_("solved"))
    last_modified_by = models.ForeignKey(User, null=True, related_name='answers_modified', verbose_name=_("last_modified_by"))


    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return self.likes - self.dislikes

    def __str__(self):
        return '%s' % (self.question.title, )


class Tag(models.Model):
    """
    Tag - zgrupowanie podobnych pytań
    """
    questions = models.ManyToManyField(Question, blank=True, null=True, related_name='tags',
                                       verbose_name=_("questions"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return _('%s' % self.name)


class Comment(models.Model):
    """
    Komentarz do pytania lub odpowiedzi, można go dodawać dla pytania lub odpowiedzi ale tylko
    dla jednego z nich
    """
    content = models.TextField(verbose_name=_("content"))
    user = models.ForeignKey(User, related_name='comments', verbose_name=_("user"))
    set_date = models.DateTimeField(auto_now_add=True, verbose_name=_("set date"))
    last_activity = models.DateTimeField(auto_now=True, verbose_name=_("last activity"))
    likes = models.PositiveIntegerField(default=0, verbose_name=_("likes"))
    dislikes = models.PositiveIntegerField(default=0, verbose_name=_("dislikes"))
    question = models.ForeignKey(Question, blank=True, null=True, related_name='comments', verbose_name=_("question"))
    answer = models.ForeignKey(Answer, null=True, blank=True, related_name='comments', verbose_name=_("answer"))
    last_modified_by = models.ForeignKey(User, null=True, related_name='comments_modified', verbose_name=_("last_modified_by"))

    def clean(self):
        if self.question and self.answer:
            raise ValidationError('Comment have to has question or answer')
        if not self.question and not self.answer:
            raise ValidationError('Comment have to has question or answer')

    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return self.likes - self.dislikes

    def __str__(self):
        return '%s' % (self.content, )


class UserProfile(models.Model):
    """
    Profil użytkownika tworzony równocześnie z użytkownikiem
    """
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/blank-profile.jpg', null=True,
                                blank=True, verbose_name=_("picture"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))

    def __str__(self):
        return _('%s' % self.user.username)


class UserPreferences(models.Model):
    """
    Preferencje użytkownika zawierają listy lubianych i nielubianych pytań, odpowiedzi, i komentarzy
    """
    user = models.OneToOneField(User)
    favorite_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="favorite_questions",
                                                verbose_name=_("favorite questions"))
    liked_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="liked_questions",
                                             verbose_name=_("liked questions"))
    disliked_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="disliked_questions",
                                                verbose_name=_("disliked questions"))
    liked_answers = models.ManyToManyField(Answer, null=True, blank=True, related_name='liked_answers',
                                           verbose_name=_("liked answers"))
    disliked_answers = models.ManyToManyField(Answer, null=True, blank=True, related_name='disliked_answers',
                                              verbose_name=_("disliked answers"))
    liked_comments = models.ManyToManyField(Comment, null=True, blank=True, related_name='liked_comments',
                                            verbose_name=_("liked comments"))
    disliked_comments = models.ManyToManyField(Comment, null=True, blank=True,
                                               related_name='disliked_comments', verbose_name=_("disliked comments"))

    def __str__(self):
        return '%s' % self.user.username

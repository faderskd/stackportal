from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    """
    Tag - zgrupowanie podobnych pytań
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return _('%s' % self.name)


class Category(models.Model):
    """
    Kategoria tematyczna
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return _('%s' % self.name)


class Question(models.Model):
    """
    Pytanie
    """
    title = models.CharField(max_length=300, unique=True, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    user = models.ForeignKey(User, blank=False, null=False)
    set_date = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    favorites = models.PositiveIntegerField(default=0)


    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return (self.likes - self.dislikes)

    def __str__(self):
        return _('%s' % self.title)


class Answer(models.Model):
    """
    Odpowiedź do pytania, user nie może odpowiadać więcej niż raz na dane pytanie
    może tylko edytować
    """
    content = models.TextField(blank=False)
    question = models.ForeignKey(Question, blank=True, null=True)
    user = models.ForeignKey(User, blank=False, null=False)
    set_date = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    solved = models.BooleanField(default=False)

    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return self.likes - self.dislikes

    def __str__(self):
        return '%s' % (self.question.title)


class Comment(models.Model):
    """
    Komentarz do pytania lub odpowiedzi, można go dodawać do dowolnego modelu
    """
    content = models.TextField(blank=False)
    user = models.ForeignKey(User, blank=False, null=False)
    set_date = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def edited(self):
        return (self.last_activity - self.set_date).seconds > 60

    def likebalance(self):
        return self.likes - self.dislikes

    def __str__(self):
        return '%s' % (self.content_object.__str__())

sda
class UserProfile(models.Model):
    """
    Profil użytkownika tworzony równocześnie z użytkownikiem
    """
    user = models.OneToOneField(User, null=False)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/blank-profile.jpg', null=True,
                                blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return _('%s' % self.user.username)


class UserPreferences(models.Model):
    """
    Preferencje użytkownika zawierają listy lubianych i nielubianych pytań, odpowiedzi, i komentarzy
    """
    user = models.OneToOneField(User, null=False)
    favorite_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="favorite_questions")
    liked_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="liked_questions")
    disliked_questions = models.ManyToManyField(Question, null=True, blank=True, related_name="disliked_questions")
    liked_answers = models.ManyToManyField(Answer, null=True, blank=True, related_name='liked_answers')
    disliked_answers = models.ManyToManyField(Answer, null=True, blank=True, related_name='disliked_answers')
    liked_comments = models.ManyToManyField(Comment, null=True, blank=True, related_name='liked_comments')
    disliked_comments = models.ManyToManyField(Comment, null=True, blank=True,
                                               related_name='disliked_comments')

    def __str__(self):
        return '%s' % self.user.username
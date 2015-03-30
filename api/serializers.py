from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import UserProfile, UserPreferences, Category, \
    Tag, Question, Answer, Comment


class UserSerializer(serializers.ModelSerializer):
    """
    Serializator usera, gdy żądanie jest typu GET password jest usuwane z serializacji
    """

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        UserPreferences.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def __delete__(self, instance):
        UserProfile.objects.get(user=instance).delete()


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializator profilu usera, dopuszczalna edycja avatara
    """

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'user', 'picture', 'created',)
        read_only_fields = ('user', 'created',)


class UserPreferencesSerializer(serializers.ModelSerializer):
    """
    Serializator preferencji użytkownika nie dopuszczamy edycji polubień, gdyż to wykonujemy w specjalnych
    operacjach put
    """

    class Meta:
        model = UserPreferences
        fields = ('id', 'url', 'user', 'favorite_questions', 'liked_questions', 'disliked_questions', 'liked_answers',
                  'disliked_answers', 'liked_comments', 'disliked_comments',)
        read_only_fields = (
        'user', 'favourite_questions', 'liked_questions', 'disliked_questions', 'liked_answers', 'disliked_answers',
        'liked_comments', 'disliked_comments',)


class TagSerializer(serializers.ModelSerializer):
    """
    Serializator tagu wraz z całą listą pytań do niego przypisanych w postaci id pytania
    """

    class Meta:
        model = Tag
        fields = ('id', 'url', 'name', 'questions',)
        read_only_fields = ('questions',)


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializator kategori wraz z listą pytań do niej przypisanych w postaci id pytania
    """

    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'questions',)
        read_only_fields = ('question_set',)


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializator pytania wraz z listą odpowiedzi i komentarzy
    """

    class Meta:
        model = Question
        fields = (
            'id', 'url', 'title', 'content', 'category',
            'tags', 'user', 'set_date', 'last_activity',
            'solved', 'views', 'likes', 'dislikes',
            'favorites', 'answers', 'comments',
        )
        read_only_fields = (
            'user', 'set_date', 'last_activity', 'solved',
            'views', 'likes', 'dislikes', 'favorites', 'answers',
            'comments',
        )


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializator pytania wraz z listą komentarzy
    """

    class Meta:
        model = Answer
        fields = (
            'id', 'url', 'content', 'question', 'user', 'set_date', 'last_activity', 'likes', 'dislikes', 'solved',
            'comments',
        )
        read_only_fields = (
            'user', 'set_date', 'last_activity', 'likes', 'dislikes', 'solved', 'comments',
        )


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializator komentarza
    """

    class Meta:
        model = Comment
        fields = (
            'id', 'url', 'content', 'user', 'set_date', 'last_activity', 'likes', 'dislikes', 'question', 'answer',
        )
        read_only_fields = (
            'user', 'set_date', 'last_activity', 'likes', 'dislikes',
        )
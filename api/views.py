from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from api.serializers import UserSerializer, UserProfileSerializer, UserPreferencesSerializer, TagSerializer, \
    CategorySerializer, QuestionSerializer, AnswerSerializer, CommentSerializer
from api.permissions import IsAccountOwnerOrIsAdminOrReadOnly, IsOwnerOrIsAdminOrReadOnly, IsAdminOrReadOnly
from api.models import UserProfile, UserPreferences, Tag, Category, Question, Answer, Comment
from rest_framework import mixins


class UserViewSet(viewsets.ModelViewSet):
    """
    Odpowiada za poszczególnych użytkowników oraz operacje na ich kontach
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAccountOwnerOrIsAdminOrReadOnly,)


class UserProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.ListModelMixin):
    """
    Wyświetlanie profilu użytkownika, dopuszczalna edycja avatara
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrIsAdminOrReadOnly,)


class UserPreferencesViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """
    Wyświetlanie prferencji użytkownika dopuszczalne tylko przeglądanie, edycja zachodzi automatycznie
    """

    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer

#TODO prawa do tagów
class TagViewSet(viewsets.ModelViewSet):
    """
    Wyświetla tagi
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Wyświetla kategorie prawa ma tylko administrator
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Wyświetla pytania edytuje tylko właściciel
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#TODO prawa do odpowiedzi
class AnswerViewSet(viewsets.ModelViewSet):
    """
    Wyświetla odpowiedzi
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Wyświetla komentarze edytuje właściciel
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



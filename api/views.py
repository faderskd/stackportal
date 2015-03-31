from django.contrib.auth.models import User
from api.serializers import UserSerializer, UserProfileSerializer, UserPreferencesSerializer, TagSerializer, \
    CategorySerializer, QuestionSerializer, AnswerSerializer, CommentSerializer
from api.permissions import IsAccountOwnerOrIsAdminOrReadOnly, IsOwnerOrIsAdminOrReadOnly, IsAdminOrReadOnly
from api.models import UserProfile, UserPreferences, Tag, Category, Question, Answer, Comment
from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

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


# TODO prawa do tagów
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
    Wyświetla pytania, edytuje tylko właściciel, dodatkowe metody pozwalają na polubienie
    lub odlubienie pytania i jak polubiamy to automatycznie odlubienie jest usuwane i w drugą stronę
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['put'])
    def like(self, request, pk):
        question = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = question.user == request.user
        if question not in user_preferences.liked_questions.all() and not is_owner:
            if question in user_preferences.disliked_questions.all():
                question.dislikes -= 1
                user_preferences.disliked_questions.remove(question)
            question.likes += 1
            question.save()
            user_preferences.liked_questions.add(question)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied

    @detail_route(methods=['put'])
    def dislike(self, request, pk):
        question = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = question.user == request.user
        if question not in user_preferences.disliked_questions.all() and not is_owner:
            if question in user_preferences.liked_questions.all():
                question.likes -= 1
                user_preferences.liked_questions.remove(question)
            question.dislikes += 1
            question.save()
            user_preferences.disliked_questions.add(question)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied

    @detail_route(methods=['put'])
    def favorite(self,request,pk):
        question = self.get_object()
        user_preference = UserPreferences.objects.get(user=request.user)
        is_owner = question.user == request.user
        if question not in user_preference.favorite_questions.all() and not is_owner:
            question.favorites += 1
            question.save()
            user_preference.favorite_questions.add(question)
            user_preference.save()
            return Response(status=200)
        else:
            raise PermissionDenied

    @detail_route(methods=['put'])
    def remove_favorite(self,request,pk):
        question = self.get_object()
        user_preference = UserPreferences.objects.get(user=request.user)
        is_owner = question.user == request.user
        if question in user_preference.favorite_questions.all() and not is_owner:
            question.favorites -= 1
            question.save()
            user_preference.favorite_questions.remove(question)
            user_preference.save()
            return Response(status=200)
        else:
            raise PermissionDenied

# TODO prawa do odpowiedzi
class AnswerViewSet(viewsets.ModelViewSet):
    """
    Wyświetla odpowiedzi , edytuje właściciel , dodatkowe metody pozwalają na polubienie
    lub odlubienie odpowiedzi i jak polubiamy to automatycznie odlubienie jest usuwane i w drugą stronę
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @detail_route(methods=['get'])
    def like(self, request, pk):
        answer = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = answer.user == request.user
        if answer not in user_preferences.liked_answers.all() and not is_owner:
            if answer in user_preferences.disliked_answers.all():
                answer.dislikes -= 1
                user_preferences.disliked_answers.remove(answer)
            answer.likes += 1
            answer.save()
            user_preferences.liked_answers.add(answer)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied

    @detail_route(methods=['put'])
    def dislike(self, request, pk):
        answer = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = answer.user == request.user
        if answer not in user_preferences.disliked_answers.all() and not is_owner:
            if answer in user_preferences.liked_answers.all():
                answer.likes -= 1
                user_preferences.liked_answers.remove(answer)
            answer.dislikes += 1
            answer.save()
            user_preferences.disliked_answers.add(answer)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied


class CommentViewSet(viewsets.ModelViewSet):
    """
    Wyświetla komentarze, edytuje właściciel, dodatkowe metody pozwalają na polubienie
    lub odlubienie komentarza i jak polubiamy to automatycznie odlubienie jest usuwane i w drugą stronę
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrIsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @detail_route(methods=['put'])
    def like(self, request, pk):
        comment = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = comment.user == request.user
        if comment not in user_preferences.liked_comments.all() and not is_owner:
            if comment in user_preferences.disliked_comments.all():
                comment.dislikes -= 1
                user_preferences.disliked_comments.remove(comment)
            comment.likes += 1
            comment.save()
            user_preferences.liked_comments.add(comment)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied

    @detail_route(methods=['put'])
    def dislike(self, request, pk):
        comment = self.get_object()
        user_preferences = UserPreferences.objects.get(user=request.user)
        is_owner = comment.user == request.user
        if comment not in user_preferences.disliked_comments.all() and not is_owner:
            if comment in user_preferences.liked_comments.all():
                comment.likes -= 1
                user_preferences.liked_comments.remove(comment)
            comment.dislikes += 1
            comment.save()
            user_preferences.disliked_comments.add(comment)
            user_preferences.save()
            return Response(status=200)
        else:
            raise PermissionDenied



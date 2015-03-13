from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from api.serializers import UserSerializer, UserProfileSerializer
from api.permissions import IsAccountOwnerOrIsAdminOrReadOnly,IsOwnerOrIsAdminOrReadOnly
from api.models import UserProfile
from rest_framework import mixins

class UserViewSet(viewsets.ModelViewSet):
    """
    Odpowiada za poszczególnych użytkowników oraz operacje na ich kontach
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAccountOwnerOrIsAdminOrReadOnly,)


class UserProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin):
    """
    Wyświetlanie profilu użytkownika, dopuszczalna edycja avatara
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrIsAdminOrReadOnly,)




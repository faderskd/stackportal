from rest_framework import permissions

class IsAccountOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do konta, jeżeli user jest właścicielem i jest zalogowany
    może edytować, w przeciwnym wypadku może tylko przeglądać
    admin może usuwać konta
    Do widoku mogą wszycy wysylać POST
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        return request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        return obj == request.user


class IsOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do obiektu i widoku, jeżeli user jest właścicielem i jest zalogowany
    może edytować w przeciwnym wypadku może tylko przeglądać
    Admin może usuwać
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        if request.method == 'PUT' and request.user.is_active and (request.user != obj.user):
            return True
        return request.user == obj.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Wszyscy poza adminem mają prawa tylko do odczytu
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAdminOrIsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Wszyscy niezalogowani mają prawa tylko do odczytu
    Zalogowani mogą tworzyć
    Admin dodatkowo może modyfikować i usuwać
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST' and request.user.is_active:
            return True
        return request.user.is_staff
from rest_framework import permissions

class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do konta, jeżeli user jest właścicielem i jest zalogowany
    może edytować, w przeciwnym wypadku może tylko przeglądać
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do profilu, jeżeli user jest właścicielem i jest zalogowany
    może edytować, w przeciwnym wypadku może tylko przeglądać
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
from rest_framework import permissions


class IsAccountOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do konta, jeżeli user jest właścicielem i jest zalogowany
    może edytować, w przeciwnym wypadku może tylko przeglądać
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


class IsOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    """
    Odpowiada za prawa do obiektu, jeżeli user jest właścicielem i jest zalogowany
    może edytować w przeciwnym wypadku może tylko przeglądać
    Admin może usuwać
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Wszyscy poza adminem mają prawa tylko do odczytu
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsQuestionAuthorOrHasAnsweredOrIsReadOnly(permissions.BasePermission):
    """

    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        if request.method == 'POST':
            has_answered = obj.question.answer_set.filter(user=request.user)
            if has_answered:
                return False
        return obj.user == request.user
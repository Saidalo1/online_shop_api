from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsOwnerOrIsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user:
            if request.user.is_staff:
                return True
            return obj.user == request.user

        return False

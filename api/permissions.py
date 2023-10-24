from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "ADMIN")


class IsVet(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "USER")
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to view or edit it.
    Assumes the model instance has an `owner` or `user` attribute.
    """

    def has_permission(self, request, view):
        # Allow any authenticated user to view their own todos
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request if the user is authenticated
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user

        # Instance must have an attribute named `user`.
        return obj.user == request.user
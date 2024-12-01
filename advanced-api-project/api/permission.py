from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
        # Custom permission to only allow authors of a book to edit it.
        def has_object_permission(self, request, view, obj):  
            if request.method in permissions.SAFE_METHODS:
                return True   # Allow Read only access to every one.
            return obj.author == request.user # Write permissions are only allowed to the author of the book

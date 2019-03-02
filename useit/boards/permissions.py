from rest_framework import permissions


class IsBoardOwner(permissions.BasePermission):
    """
    Custom permission to evaluate if a board is private and act accordingly
    """

    def has_object_permission(self, request, view, obj):

        if obj.isPrivate:
            return obj.owner == request.user
        else:    
            if obj.owner == request.user:
                return True
            # If public, read permissions are allowed to any user,
            # so we'll always allow GET, HEAD or OPTIONS requests.
            if request.method in permissions.SAFE_METHODS:
                return True

class IsOwnerOrPublicBoard(permissions.BasePermission):
    """
    Custom permission to evaluate if a note can be created
    """

    def has_object_permission(self, request, view, obj):

        if obj.board.isPrivate:
            return obj.board.owner == request.user

        # If the board is public, users are able to Read 
        # and Create notes
        if request.method in (permissions.GET, permissions.POST):
            return True            
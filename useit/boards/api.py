from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import BoardSerializer, NoteSerializer
from .models import Board, Note

from .permissions import IsBoardOwner, IsOwnerOrPublicBoard
 
 
class BoardViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsBoardOwner,)
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
 
 
class NoteViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrPublicBoard,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
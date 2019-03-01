from rest_framework.viewsets import ModelViewSet
from .serializers import BoardSerializer, NoteSerializer
from .models import Board, Note
 
 
class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
 
 
class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
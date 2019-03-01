from rest_framework.serializers import ModelSerializer
from .models import Board, Note
 
 
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'text', 'board',)

class BoardSerializer(ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Board
        fields = ('name', 'notes',)

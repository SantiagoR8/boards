from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Board, Note
 
 
class NoteSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    def create(self, validated_data):
        data = validated_data.copy()
        data['owner'] = self.context['request'].user

        return super(NoteSerializer, self).create(data)

    class Meta:
        model = Note
        fields = ('title', 'text', 'board')

class BoardSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    def create(self, validated_data):
        data = validated_data.copy()
        data['owner'] = self.context['request'].user

        return super(BoardSerializer, self).create(data)

    class Meta:
        model = Board
        fields = ('name', 'isPrivate', 'notes',)

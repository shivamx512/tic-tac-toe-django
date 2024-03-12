from rest_framework import serializers
from game.models import Game

class GameSerializer(serializers.ModelSerializer):
    """Serializer for Game objects"""

    class Meta:
        model = Game
        fields = '__all__'
        depth = 1
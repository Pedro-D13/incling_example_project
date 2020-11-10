from incling_example.settings import DATE_FORMAT
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from research_software.models import TaskObject, TileObject


class TaskObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskObject
        fields = ["id", "Title", "Description", "Order", "Type", "Tile"]
        validators = [
            UniqueTogetherValidator(
                queryset=TaskObject.objects.all(), fields=["Order", "Tile"]
            )
        ]


class TileObjectSerializer(serializers.ModelSerializer):
    Launch_data = serializers.DateField(format=DATE_FORMAT)
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = TileObject
        fields = ["Launch_data", "Status", "tasks"]

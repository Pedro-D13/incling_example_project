from rest_framework import serializers

from research_software.models import TaskObject, TileObject


class TaskObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskObject
        fields = ["id", "Title", "Description", "Order", "Type", "Tile"]


class TileObjectSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = TileObject
        fields = ["id", "Launch_data", "Status", "tasks"]

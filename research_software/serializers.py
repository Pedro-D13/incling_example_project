from incling_example.settings import DATE_FORMAT
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from research_software.models import TaskObject, TileObject


class TaskObjectSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="task-detail")
    Tile = serializers.HyperlinkedRelatedField(
        view_name="tile-detail", queryset=TileObject.objects.all()
    )

    class Meta:
        model = TaskObject
        fields = ["id", "Title", "Description", "Order", "Type", "Tile"]
        validators = [
            UniqueTogetherValidator(
                queryset=TaskObject.objects.all(), fields=["Order", "Tile"]
            )
        ]


class TileObjectSerializer(serializers.ModelSerializer):
    Launch_date = serializers.DateField(format=DATE_FORMAT)
    tasks = serializers.StringRelatedField(many=True, read_only=True)
    id = serializers.HyperlinkedIdentityField(view_name="tile-detail")

    class Meta:
        model = TileObject
        fields = [
            "id",
            "Launch_date",
            "Status",
            "tasks",
        ]

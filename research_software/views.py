from django.shortcuts import get_object_or_404, render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from research_software.models import TaskObject, TileObject
from research_software.serializers import TaskObjectSerializer, TileObjectSerializer


# Create your views here.
class TaskObjectViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TaskObject.objects.all()
    serializer_class = TaskObjectSerializer


class TileObjectViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TileObject.objects.all()
    serializer_class = TileObjectSerializer

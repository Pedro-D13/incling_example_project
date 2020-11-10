from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskObjectViewSet, TileObjectViewSet

router = DefaultRouter()
router.register(r"tasks", TaskObjectViewSet, basename="task")
router.register(r"tile", TileObjectViewSet, basename="tile")

urlpatterns = []
urlpatterns += router.urls

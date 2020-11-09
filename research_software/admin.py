from django.contrib import admin

from .models import TaskObject, TileObject


# Register your models here.
class TaskObjAdmin(admin.ModelAdmin):
    pass


class TileObjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(TaskObject, TaskObjAdmin)
admin.site.register(TileObject, TileObjectAdmin)

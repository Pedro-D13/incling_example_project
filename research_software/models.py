from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class TileObject(models.Model):

    status_options = [
        ("live", "Live"),
        ("pending", "Pending"),
        ("archived", "Archived"),
    ]
    Launch_data = (
        models.DateField()
    )  # could also be a datatime field depending on the full use case but this wasn't made explicit
    Status = models.CharField(choices=status_options, default="pending", max_length=10)

    class Meta:
        ordering = ["-Launch_data"]

    lookup_field = "tile"

    def __str__(self):
        try:
            num_of_tasks = self.taskobject_set.all().count()
            return f"Status:{self.Status}, Launch:{self.Launch_data:%b %d %Y}, # of Tasks:{num_of_tasks}"
        except (NameError, AttributeError):
            pass
        return f"Status:{self.Status}, Launch:{self.Launch_data:%b %d %Y}"


class TaskObject(models.Model):
    types_of_options = [
        ("survey", "Survey"),
        ("discussion", "Discussion"),
        ("diary", "Diary"),
    ]

    OrderOptions = [
        ("1", "postion 1"),
        ("2", "postion 2"),
        ("3", "postion 3"),
        ("4", "postion 4"),
    ]
    # extend it based on the amount of questions you'd usually ask

    Title = models.CharField(
        max_length=50, unique=True
    )  # titles do not usually require to be long
    Description = (
        models.TextField()
    )  # Accepts an arbitrary amount of text, allowing for varying lengths of description.
    Order = models.IntegerField(
        choices=OrderOptions, default=None, null=True, blank=True, unique=False
    )  #  setting the blank=True allows the order to be set a later date
    Type = models.CharField(choices=types_of_options, max_length=10, default="survey")
    Tile = models.ForeignKey(
        TileObject,
        related_name="tasks",
        on_delete=models.CASCADE,
    )

    class meta:
        ordering = ["-Order", "Type"]

    def __str__(self):
        return f"Title:{self.Title}, Desc:{self.Description},Position:{self.Order},Type:{self.Type}"

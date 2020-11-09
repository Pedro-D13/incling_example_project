from django.db import models


class TileObject(models.Model):
    status_options = [
        ("live", "Live"),
        ("pending", "Pending"),
        ("archived", "Archived"),
    ]
    Launch_data = models.DateField(
        verbose_name="Launch Data"
    )  # could also be a datatime field depending on the full use case but this wasn't made explicit
    Status = models.CharField(choices=status_options, default="pen", max_length=10)

    def __str__(self):
        try:
            num_of_tasks = self.taskobject_set.all().count()
            return f"Status:{self.Status}, Launch:{self.Launch_data}, # of Tasks:{num_of_tasks}"
        except Error:
            pass
        return f"Status:{self.Status}, Launch:{self.Launch_data}"


class TaskObject(models.Model):
    types_of_options = [("sur", "Survey"), ("dis", "Discussion"), ("dia", "Diary")]
    Title = models.CharField(
        max_length=50, unique=True
    )  # titles do not usually require to be long
    Description = (
        models.TextField()
    )  # Accepts an arbitrary amount of text, allowing for varying lengths of description.
    Order = models.IntegerField()
    Type = models.CharField(choices=types_of_options, max_length=3, default="sur")
    Tile = models.ForeignKey(TileObject, on_delete=models.CASCADE)

    class meta:
        order_with_respect_to = ["Order"]

    def __str__(self):
        return f"Title:{self.Title}, Desc:{self.Description}"

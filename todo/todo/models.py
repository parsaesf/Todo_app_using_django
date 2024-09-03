from django.db import models
from django.contrib.auth.models import User


class TODOO(models.Model):
    class Status(models.TextChoices):
        in_progress = "doing"
        done = "done"

    srno = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=250, choices=Status.choices, default=Status.in_progress
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

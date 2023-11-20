from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.

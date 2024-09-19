from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    priority = models.IntegerField()


    def __str__(self):
        return f'{self.title} - {self.task[:30]}...'
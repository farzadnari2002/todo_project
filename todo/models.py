from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title


class Todo(models.Model):
    Category = models.ManyToManyField(Category,  related_name='todos')
    title = models.CharField(max_length=100)
    task = models.TextField()
    priority = models.IntegerField()


    def __str__(self):
        return f'{self.title} - {self.task[:30]}...'
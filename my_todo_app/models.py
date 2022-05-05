from django.db import models

# Create your models here.

class TodoList(models.Model):
    my_todo = models.CharField(max_length=300)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.my_todo

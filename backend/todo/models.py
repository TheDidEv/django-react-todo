from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True)

    def __str__(self):   # return task on string format
        return self.task # self - link to curent instance of the class
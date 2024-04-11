import uuid
from account.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='exercises', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='descriptionnn')


    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name
    


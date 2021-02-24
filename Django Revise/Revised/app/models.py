from django.db import models

# Create your models here.

class User(models):

    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username
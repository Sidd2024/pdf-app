from django.db import models

# Create your models here.
class User(models.Model):
    pass

class Text(models.Model):
    text = models.TextField(default="")
    filename = models.CharField(max_length=64)
from django.db import models


# Create your models here.




class Thought(models.Model):
    thought = models.TextField()
    author = models.CharField(max_length=50)

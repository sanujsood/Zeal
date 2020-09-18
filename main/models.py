from django.db import models


# Create your models here.




class Thought(models.Model):
    thought = models.TextField()
    author = models.CharField(max_length=50)


class Schedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    description = models.TextField()
    venue = models.TextField()

    def __str__(self):
        return self.title
        
            

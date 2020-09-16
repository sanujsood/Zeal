from django.db import models


# Create your models here.
day_choices = (
   ('monday', 'monday'),
   ('tuesday', 'tuesday'),
   ('wednesday', 'wednesday'),
   ('thursday', 'thursday'),
   ('friday', 'friday'),
   ('saturday', 'saturday'),
   ('sunday', 'sunday'),
)



class Thought(models.Model):
    thought = models.TextField()
    author = models.CharField(max_length=50)
    day    = models.CharField(choices=day_choices, max_length=128)

    def __str__(self):
        return self.day

from django.db import models



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



class Schedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    description = models.TextField()
    venue = models.TextField()

    def __str__(self):
        return self.title
        
            


from django.db import models

# Create your models here.
status = (
   ('member', 'member'),
   ('developer', 'developer'),
   ('cord','cord'),
   ('fac' ,'fac'),
)

class Team(models.Model):

    name            = models.CharField(max_length=45)
    designation     = models.CharField(max_length=45)
    images          = models.ImageField(upload_to= 'images/team',default='')
    linkedin        = models.URLField()
    status          = models.CharField(choices=status, max_length=128)
    # role            = models.TextField()

    def __str__(self):
        return self.name

    

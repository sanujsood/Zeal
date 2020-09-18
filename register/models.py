from django.db import models



# Create your models here.
class Register(models.Model):

    name    = models.CharField(max_length=50)
    email   = models.EmailField()
    branch  = models.CharField(max_length=20)
    year    = models.IntegerField()
    document = models.FileField(upload_to = 'documents')   
    
    class Meta:
        db_table = "register"
    

    def __str__(self):
        return self.name

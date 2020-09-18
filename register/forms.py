from django import forms
from .models import Register

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['name','email','branch','year','document']
                                                                                                                                                                                                                                                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # name    = forms.CharField(max_length=50)
    # email   = forms.EmailField()
    # branch  = forms.CharField(max_length=20)
    # year = forms.IntegerField()
    # document = forms.FileField(upload_to= 'documents')  
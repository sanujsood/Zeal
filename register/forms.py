from django import forms
from .models import Register
from django.forms import ModelForm, Textarea ,CharField,FileField,IntegerField



class DocumentForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=('name','email','branch','year','document')
        widgets = {
            'name': Textarea(attrs={'class' : "input--style-6",'rows':1}),
            'email': Textarea(attrs={'class' : "input--style-6",'rows':1 , 'type':'email'}),
            'branch': Textarea(attrs={'class' : "input--style-6",'rows':1}),
            'year':   Textarea(attrs={'class' : "input--style-6",'rows':1,'type':'number'}),
            
        }                                                                                                                                                                                                                                       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # name    = forms.CharField(max_length=50)
    # email   = forms.EmailField()
    # branch  = forms.CharField(max_length=20)
    # year = forms.IntegerField()
    # document = forms.FileField(upload_to= 'documents')  
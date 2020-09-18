from django.shortcuts import render
from .models import Register
from register.forms  import DocumentForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    else:
        form=DocumentForm()    
   
    return render(request,'register.html',{'form':form})

        


        
    
    
    
        
    

def about(request):

    return render(request,'about.html')
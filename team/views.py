from django.shortcuts import render
from .models import Team
# Create your views here.

def about(request):

    member        = Team.objects.filter(status = 'member')
    dev           = Team.objects.filter(status = 'developer')
    coordinator   = Team.objects.filter(status = 'cord')
    faculty        = Team.objects.filter(status = 'fac')

    context = {'member':member,
                'dev':dev,
                'coordinator':coordinator,
                'faculty':faculty,
                }

    return render(request,'about.html',context)


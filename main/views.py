from django.shortcuts import render
from blog.models import Blog
from .models import Thought
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
import calendar



# Create your views here.
def home(request):

    
    
    blog    = Blog.objects.filter(trends = 'Y')
   #finding the current day   THe hard way
    day_today     = datetime.today()
    string  = str(day_today)
    year = int(string[:4])
    month = int(string[5:7])
    day = int(string[8:10])
    today  = calendar.weekday(year,month,day)
    day_name= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']

    th = Thought.objects.filter(day=day_name[today])

 

    return render(request,'index.html', {'th':th,'blog':blog})


def blog(request):

    context   = Blog.objects.all()
    paginator = Paginator(context,2)
    page = request.GET.get('page')
    try:
        context = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        context = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        context = paginator.page(paginator.num_pages)
    return render(request,'blog.html',{'context':context})


def blog_detail(request,name):
    context = Blog.objects.filter(name=name)

    return render(request,'blog-single.html',{'context':context})
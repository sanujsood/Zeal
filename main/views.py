from django.shortcuts import render
from blog.models import Blog
from events.models import Events
from .models import Thought,Schedule
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.
def home(request):

    
    
    blog    = Blog.objects.filter(trends = 'Y')
    th = Thought.objects.all()
    sch=Schedule.objects.all()

    return render(request,'index.html', {'th':th,'blog':blog,'sch':sch})


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



# def events(request):

#     context   = Events.objects.all()
#     paginator = Paginator(context,2)
#     page = request.GET.get('page')
#     try:
#         context = paginator.page(page)
#     except PageNotAnInteger:
#             # If page is not an integer deliver the first page
#         context = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         context = paginator.page(paginator.num_pages)
#     return render(request,'events.html',{'context':context})
def events_detail(request,name):
    context = Events.objects.filter(name=name)

    return render(request,'events-single.html',{'context':context})
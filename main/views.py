from django.shortcuts import render, redirect
from blog.models import Blog
from json import dumps
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
import calendar
from newsletter.models import Email
from zeal.settings import EMAIL_HOST_USER
from events.models import Events
from .models import Thought,Schedule,Videos

from datetime import date, datetime




# Create your views here.
def home(request):

    
    if request.method == 'POST':
        name = request.POST['name']
        email =request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Email(email=email)
        data.save()
        reciever = []
        reciever.append('anubhavgupta2260@gmail.com')
        send_mail("New Queries From Zeal Webapp","from "+name+email+ "\n"+message,EMAIL_HOST_USER, reciever)
        return redirect(home)




    else:
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

        event = Events.objects.filter(trends='Y')


        sch=Schedule.objects.all()
        deadline = sch[0].deadline
        dataDictionary = {'date':deadline}
        # dataJSON = dumps(dataDictionary)
        dataJSON =  dumps(deadline, default=json_serial)
        date=deadline.date
        time=deadline.time
        x=str(date)
        print(x)

        return render(request,'index.html', {'th':th,
                                            'blog':blog,
                                            'sch':sch,
                                            'event':event,
                                            'data':dataJSON})



def blog(request):

    context   = Blog.objects.all()
    paginator = Paginator(context,5)
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

    return render(request,'event-single.html',{'context':context})





def videos(request):


    videos   = Videos.objects.all()
    blog     = Blog.objects.filter(trends = 'Y')
    event    = Events.objects.filter(trends='Y')

    context = {
        'videos': videos,
        'blog':   blog,
        'event' : event

    }
    return render(request,'success-stories.html',context)





def json_serial(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
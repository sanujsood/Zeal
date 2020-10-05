from django.contrib import admin
from django.urls import path , include
from team.views import about

from tinymce import urls
from . import views

from events.views import events
from register.views import register


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blogs'),    
    path('blog/<str:name>',views.blog_detail,name='blog'),

    path('events/',events,name='events'), 
    path('events/<str:name>',views.events_detail,name='name'),
    path('register/',register,name='register'), 
    path('about/',about , name ='about'),
    path('videos/',views.videos , name ='videos'),
    path('tinymce/', include('tinymce.urls')),

     

]

from django.contrib import admin
from django.urls import path



from . import views

from events.views import events
from register.views import register


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home),
    path('blog/',views.blog,name='blogs'),    
    path('blog/<str:name>',views.blog_detail,name='name'),

    path('events/',events,name='name'), 
    path('events/<str:name>',views.events_detail,name='name'),
    path('register/',register,name='name'), 

     

]

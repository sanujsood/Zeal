from django.contrib import admin
from django.urls import path
from . import views

from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home),
    path('blog/',views.blog,name='blogs'),    
    path('blog/<str:name>',views.blog_detail,name='name'),
]

from django.contrib import admin



# Register your models here.



from .models import Thought,Schedule,Videos

# Register your models here.

admin.site.register(Thought)
admin.site.register(Schedule)
admin.site.register(Videos)


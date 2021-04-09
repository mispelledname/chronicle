from django.contrib import admin

# Register your models here.
from .models import Job
from .models import User
from .models import Tag

admin.site.register(Job)
admin.site.register(User)
admin.site.register(Tag)
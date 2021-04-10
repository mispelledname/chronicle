from django.contrib import admin

# Register your models here.
from .models import Job
from .models import UserProfile
from .models import Tag

admin.site.register(Job)
admin.site.register(UserProfile)
admin.site.register(Tag)
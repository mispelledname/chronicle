from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Job

def index(request):
    return HttpResponse("Hello, world. You're at the oddjob index.")

def detail(request, job_id):
    context = {'job': Job.objects.get(id=job_id)}
    return render(request, 'oddjob/detail.html', context)
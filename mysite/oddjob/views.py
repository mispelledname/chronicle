from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Job

def index(request):
    return HttpResponse("Hello, world. You're at the oddjob index.")

def detail(request, job_id):
    template = loader.get_template('oddjob/detail.html')
    context = {'job': Job.objects.get(id=job_id)}
    return HttpResponse(template.render(context, request))
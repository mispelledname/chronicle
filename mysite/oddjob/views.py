from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Job

def index(request):
    jobList = Job.objects.order_by('-datePosted')
    context = {'jobList':jobList}
    return render(request,'oddjob/index.html',context)

def detail(request, job_id):
    context = {'job': Job.objects.get(id=job_id)}
    return render(request, 'oddjob/detail.html', context)

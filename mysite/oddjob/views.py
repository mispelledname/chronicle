from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse,Http404

from .models import Job, User, Tag
import datetime

def index(request):
    jobList = Job.objects.order_by('-datePosted')
    context = {'jobList':jobList}
    return render(request,'oddjob/index.html',context)

def detail(request, job_id):
    try:
        context = {'job': Job.objects.get(id=job_id)}
    except:
        raise Http404("Job does not exist.")
    return render(request, 'oddjob/detail.html', context)

def user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'oddjob/user.html', context={'user':user})

def post(request):
    if request.method == 'POST':
        [h, m] = list(map(int, request.POST.get('duration').split(':')))
        job = Job(title=request.POST.get('title'),
        description=request.POST.get('description'),
        taskDuration = datetime.timedelta(hours=h, minutes=m ),
        datePosted = datetime.datetime.now(), 
        dateDue = request.POST.get('datedue'),
        numHelperRequested = request.POST.get('numHelpers'))
        job.save()
    return render(request, 'oddjob/newpost.html')


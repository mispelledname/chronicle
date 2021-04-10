from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse,Http404, HttpResponseRedirect

from .models import Job, UserProfile, Tag
import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def index(request):
    jobList = Job.objects.order_by('-datePosted')
    # TODO: add user name
    context = {'jobList':jobList, 'userName': 'Admin'}
    return render(request,'oddjob/index.html',context)

def detail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        name_collab = " ".join([e.name for e in job.contributors.all()])
        context = {'job': job, 'collab':name_collab, 'user_id':request.user.id}
    except:
        raise Http404("Job does not exist.")
    return render(request, 'oddjob/detail.html', context)

def user(request, xid):
    user = get_object_or_404(User, id=xid)
    return render(request, 'oddjob/user.html', context={'user':user})

def post(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'oddjob/newpost.html')
        elif request.method == 'POST':
            [h, m] = list(map(int, request.POST.get('duration').split(':')))
            job = Job(title=request.POST.get('title'),
            description=request.POST.get('description'),
            taskDuration = datetime.timedelta(hours=h, minutes=m ),
            datePosted = datetime.datetime.now(), 
            dateDue = request.POST.get('datedue'),
            numHelperRequested = request.POST.get('numHelpers'),
            originUser=request.user.userprofile)
            job.save()
            # return render(request, 'oddjob/newpost.html')
            return redirect('/oddjob')
    else:
        return HttpResponseRedirect('/oddjob/login')
    

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/oddjob')
        #return HttpResponseRedirect("")
    else:
        if request.method == 'GET':
            return render(request, 'oddjob/login.html', {'req': request})
        elif request.method == "POST":
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/oddjob/")
            else:
                return HttpResponseRedirect("/oddjob/login")
    pass

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/oddjob')
        #return HttpResponseRedirect("")
    else:
        if request.method == 'GET':
            return render(request, 'oddjob/register.html', {'req': request})
        elif request.method == "POST":
            username = request.POST.get("username", "")
            first_name = request.POST.get("first_name", "")
            surname = request.POST.get("surname", "")
            password = request.POST.get("password", "")

            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=surname, password=password)
            new_user.userprofile.name = first_name
            new_user.save()

            login_user = authenticate(request, username=username, password=password)
            login(request, login_user)

            return redirect('/oddjob')
            #return HttpResponseRedirect("")

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/oddjob/login')
    else:
        return HttpResponseRedirect('/oddjob/login')

def self_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(f'user/{request.user.id}/')
    else:
        return redirect('oddjob/login')

def accept_job(request, job_id, user_id):
    user = get_object_or_404(User, id=user_id)
    job = get_object_or_404(Job, id=job_id)
    job.contributors.add(user.userprofile)
    return redirect(f'/oddjob/{job_id}')

def mytasks(request):
    if request.user.is_authenticated:
        my_creations = Job.objects.filter(originUser=request.user.userprofile)
        contributions = Job.objects.filter(contributors=request.user.userprofile)
        return render(request, 'oddjob/mytasks.html', {'myposts': my_creations, 'contributions': contributions})
    else:
        return redirect('/oddjob/login')
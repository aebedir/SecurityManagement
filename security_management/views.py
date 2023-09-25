from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def index(request):
    guards = SecurityGuard.objects.all()    
    times = []
    for guard in guards:
        time = DutyTime.objects.get(guard=guard)
        times.append(time)

    guard_list = zip(guards, times)
    
    if request.method == "POST":        
        guard_id = request.POST.get("guardId")
        time_id = request.POST.get("timeId")
       
        guard = SecurityGuard.objects.get(id=guard_id)
        time = DutyTime.objects.get(id=time_id)
        
        guard.delete()
        time.delete()
        
        return JsonResponse(data={'success':'Deleted'})    
    context = {
        'guard_list': guard_list,
        'guards':guards,
    }
    return render(request, 'index.html', context)


def securityGuards(request):   
    
    if request.method=="POST":
        name = request.POST['name']
        surname = request.POST['surname']
        date = request.POST['date']
        experience = request.POST['experience']
        start = request.POST['start']
        end = request.POST['end']

        
        guards = SecurityGuard(
            name=name,
            surname=surname,
            date_of_birth=date,
            years_of_experience=experience,            
        )
        guards.save()

        time = DutyTime(
            start_time = start,
            end_time=end,
            guard = guards
        )
        time.save()
        
        messages.success(request,'Security Guard Added')
        return redirect('index')
    
    return render(request,'security_guards.html')

from django.http import JsonResponse

def editTime(request,timeId):

    if request.method=="POST":
        time = DutyTime.objects.get(id = timeId)
        start = request.POST['start']
        end = request.POST['end']
        time.start_time = start
        time.end_time=end

        time.save()
        return redirect('index')
    return render(request,'edit.html')
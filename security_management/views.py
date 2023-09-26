from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse

def index(request):    
    guards = SecurityGuard.objects.all()   
        
    if request.method == "POST":      
        guard_id = request.POST['guardId']
        guard = SecurityGuard.objects.get(id=guard_id)
        guard.delete()
        
        
        return JsonResponse(data={'success':'Deleted'})    
    context = {        
        'guards':guards,        
    }
    return render(request, 'index.html', context)


def securityGuards(request):   
    places = Place.objects.all()
    duty_times = DutyTime.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        date = request.POST['date']
        experience = request.POST['experience']
        selected_time = request.POST['time']         
        place_id = request.POST['place']

        place = Place.objects.get(pk=place_id)         
        duty_time = DutyTime.objects.get(time=selected_time) 
        
        guards = SecurityGuard(
            name=name,
            surname=surname,
            date_of_birth=date,
            years_of_experience=experience,
            guard_place=place,  
            duty_times=duty_time  
        )
        guards.save()        
        
        messages.success(request, 'Security Guard Added')
        return redirect('index')
    
    context = {
        'places': places,
        'duty_times': duty_times
    }

    return render(request, 'security_guards.html', context)



def editTime(request,guardId):
    places = Place.objects.all()
    duty_times = DutyTime.objects.all()
    guard = SecurityGuard.objects.get(id = guardId )
    if request.method == "POST":
        place_id = request.POST['place']
        time_id = request.POST['time']
        
        guard.guard_place = Place.objects.get(id=place_id)
        guard.duty_times = DutyTime.objects.get(time=time_id)
        guard.save()

        messages.success(request, 'Security Guard Edited')
        return redirect('index')
    context = {
        'places': places,
        'duty_times': duty_times,
        'guard':guard
    }
    return render(request,'edit.html',context)
from django.core.management import call_command
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def start_scheduler(request):
    call_command('runapscheduler')
    return HttpResponse('APScheduler started')

def stop_scheduler(request):
    return HttpResponse('APScheduler cant be stopped because i am tired to find a solution to do it :(')

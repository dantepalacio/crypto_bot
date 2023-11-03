from django.core.management import call_command
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from cryptonews_app.task import run_selenium_task
import subprocess

def home(request):
    return render(request, 'home.html')


def start_scheduler(request):
    call_command('runapscheduler')
    return HttpResponse('APScheduler started')

def stop_scheduler(request):
    return HttpResponse('APScheduler cant be stopped because i am tired to find a solution to do it :(')



# def parse_and_save_news(request):
#     run_selenium_task()
#     return render(request, "crypto_parse.html")


def run_puppeteer(request):
    script_path = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\cryptonews_app\\static\\js\\crypto_news.js"
    
    try:
        result = subprocess.check_output(['node', script_path], universal_newlines=True)
        return render(request, 'puppeteer_result.html', {'result': result})
    except Exception as e:
        error_message = f"Найдена ошибка: {str(e)}"
        return HttpResponse(error_message, status=500)
    

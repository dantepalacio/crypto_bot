from django.core.management import call_command
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from cryptonews_app.task import run_selenium_task
from .models import CryptoNews
import subprocess
import psycopg2

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
    

def get_news_from_db(request):
    conn = psycopg2.connect(
        user = "postgres",
        password = "Qwertyu123451!",
        host = "localhost",
        database = "postgres",
        port = 5432
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news")
    
    news = []
    for item in cursor.fetchall():
        news_item = {
            "id": item[0],
            "crypto_name": item[1],
            "title": item[2],
            "content": item[3],
        }
        news.append(news_item)

    conn.close()

    return render(request, "news_from_pg.html", {"news": news})
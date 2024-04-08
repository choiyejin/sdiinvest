from django.shortcuts import render
from .models import News

# Create your views here.
def get_news(requests):
    news = News.objects.all()
    return render(requests, "table.html", {"news_array" : news})
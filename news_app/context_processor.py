from .models import *

def latest_news(request):
    news = News.published.all().order_by('-published_time')[:10]
    context = {
        'news':news
    }
    return context

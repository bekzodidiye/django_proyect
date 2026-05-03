from django.urls import  path

from  .views import *





urlpatterns = [
    path('', HomePageView.as_view(), name='all_news_list'),
    path('<slug:news>/',news_detail,name='news_detail_page'),
    path('about/',about,name='about_page'),
    path('contact',ContactView.as_view(),name='contact_page'),
    path('category',category,name='category_page'),
    path('latest',latest_news,name='latest_news_page'),
    

]
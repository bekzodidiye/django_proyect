from django.views.generic import UpdateView
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *
from django.views.generic import TemplateView,UpdateView,ListView,DeleteView,CreateView


# def news_list(request):
#     featured_news = News.objects.filter(is_featured=True)
#     latest_news = News.published.all()[:10]
#     category_news1 = News.objects.filter(category__name="Olam").order_by('-published_time')[:1]
#     category_news2 = News.objects.filter(category__name="Jamiyat").order_by('-published_time')[:1]
#     category_news3 = News.objects.filter(category__name="Sport").order_by('-published_time')[:1]

#     categories =Category.objects.all()
#     context= {
#         'featured_news':featured_news,
#         'latest_news':latest_news,
#         'category_news1':category_news1,
#         'category_news2':category_news2,
#         'category_news3':category_news3,
#         'categories':categories,
#     }
        
#     return render(request, 'news/index.html',context)
class HomePageView(ListView):
    model = News        
    template_name = 'news/index.html'
    context_object_name = 'news_list'
    queryset = News.published.all()
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_news'] = News.objects.filter(is_featured=True)
        context['latest_news'] = News.published.all()[:10]
        context['category_news1'] = News.objects.filter(category__name = 'Olam').order_by('-published_time')[:1]
        context['category_news2'] = News.objects.filter(category__name = "Jamiyat").order_by('-published_time')[:1]
        context['category_news3'] = News.objects.filter(category__name = "Sport").order_by('-published_time')[:1]
        context['categories'] = Category.objects.all()
        return context

def news_detail(requests,news):
    news = get_object_or_404(News,slug=news,status=News.Status.Published)
    context = {
        'news':news
    }
    
    return render(requests,'news/details.html',context)

def about(request):
    context ={}
    return render(request,'news/about.html',context)

# def contact(request):
#     form = ContactForm(request.POST)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('contact_page')
#     context={
#         'form':form
#     }
#     return render(request,'news/contact.html',context)
class ContactView(TemplateView):
    
    model = Contact
    template_name = 'news/contact.html'
    
    def get(self,requests,*args,**kwargs):
        form = ContactForm()
        context= {
            'form':form
        }
        return render(requests,'news/contact.html',context)
    def post(self,requests,*args,**kwargs):
        form = ContactForm(requests.POST)
        if requests.method == 'POST' and form.is_valid:
            form.save()
            return redirect('contact_page')
        context = {
             'form':form
        }
        return render(requests,'news/contact.html',context)

def category(request):
    categories=Category.objects.all()
    context={
     'categories':categories
    }
    return render(request,'news/categori.html',context)
def latest_news(request):
    context = {}
    return render(request,'news/latest_news.html',context)


class News_update_view(UpdateView):
    model = News
    fields = ['title', 'slug', 'body', 'image', 'category', 'status']
    template_name = 'crud/news_edit.html'

class News_create_view(CreateView):
    model = News
    fields = ['title', 'slug', 'body', 'image', 'category', 'status']
    template_name = 'crud/news_create.html'
    

class News_delete_view(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('all_news_list')


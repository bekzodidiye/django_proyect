from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def user_login(request):   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data 
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('all_news_list')
                else:
                    return render(request, 'accounts/login.html', {'form': form, 'error': 'Akkaunt faol emas'})
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Login yoki parolda xatolik bor'})
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
def user_profile(request):
    user = request.user
    context= {
         'user':user,
    }
    return render(request,'pages/user_profile.html',context)



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['confirm_password'])
            user.save()
            login(request,user)
            return redirect('all_news_list')
        else:
            context={
                'form':form
            }
            return render(request,'accounts/signup.html',context)

    else:
        form = UserRegistrationForm()
        context={
             'form':form
        }
        return render(request,'accounts/signup.html',context)


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name='accounts/signup.html'


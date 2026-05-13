from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm

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
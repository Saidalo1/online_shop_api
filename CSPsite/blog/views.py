from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, template_name='login.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})

def logout_request(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse_lazy("index"))

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        form = RegisterForm(data=request.POST)
        if form.is_valid():

            user = form.instance
            user.set_password(request.POST['password'])
            form.save()

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, template_name='register.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})
        
        return render(request, template_name='register.html', context={'form': form})
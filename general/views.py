from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from general.email_backend import EmailBackend
from general.models import CustomUser
from general.forms import CustomUserForm
from django.contrib import messages

# Create your views here.

def homepage(request):
    context = {}
    return render(request, 'general/index.html', context)

def about_us(request):
    context = {
    }
    return render(request, 'general/about.html', context)



def service(request):
    context = {}
    return render(request, 'general/services.html', context)

def portfolio(request):
    context = {}
    return render(request, 'general/portfolio.html', context)

def login_page(request):
     context = {
        'title': 'Login'
    }
     if request.POST:
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = EmailBackend.authenticate(request, username=username, password=password)
         if user is None:
             messages.error(request, 'invalid username/password')
             return redirect(reverse('login'))
         else:
             login(request, user)
             messages.success(request, 'Access granted')
             return redirect(reverse('dashboard'))
     return render(request, 'general/loginpage.html', context)

def logout_page(request):
    try:
        logout(request)
        messages.success(request, 'Logged out')
        return redirect(reverse('login'))
    except:
        pass
    return redirect(reverse('login'))

def dashboard(request):
    context = {
        'real_estates':  CustomUser.objects.all(),
        'title': 'Dashboard'
    }
    if request.user.is_authenticated:
     return render(request, 'general/dashboard.html', context)
    else:
        return redirect(reverse('login'))  
     
 
def register(request):
    form = CustomUserForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'title': 'Registration'
    }
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect(reverse('login'))
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'general/registration.html', context)
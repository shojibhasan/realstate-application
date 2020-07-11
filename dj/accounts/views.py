from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from listings import views

# Create your views here.
from django.urls import reverse
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken!')
                else:
                    User.objects.create_user(username=username,
                                             password=password,
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email
                                             )
                    messages.success(request, 'You are successfully registered!')
                    return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Password does not match!')

        return HttpResponseRedirect(reverse('register'))

    #	return redirect('user-register') # not standard

    return render(request, 'accounts/register.html')


def login(request):
    if request.method =="POST":
        method_dict = request.POST.copy()

        username = method_dict.get('username')

        password = method_dict.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You sucessfully login')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid Credential!')
            return HttpResponseRedirect(reverse('login'))

    return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')


def logout(request):
    if request.method =="POST":
        auth.logout(request)
        messages.error(request, 'You are now loggd out')
        return HttpResponseRedirect(reverse('index'))
    #return HttpResponseRedirect(reverse('index'))

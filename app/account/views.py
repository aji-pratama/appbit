from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'account/dashboard.html')

def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff = False
        u = User.objects.create_user(username=username, password=password, email=email)
        u.first_name = first_name
        u.last_name = last_name
        u.is_staff = staff
        u.save()
        return HttpResponseRedirect('/')
    return render(request, 'account/register.html')

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            #For Admin / Staff
            return HttpResponse("Login Berhasil ini staff")
        elif user is not None:
            #For costumer
            return HttpResponse("Login Berhasil ini Bukan staff")
        else:
            return HttpResponse("Login Gagal")
    return render(request, 'account/login.html')

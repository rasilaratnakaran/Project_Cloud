from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user
from .models import enquiry
from django.contrib import messages
from django.contrib.auth import authenticate, login
 
from django.template import loader
 
# Create your views here.
def home(request):
        return render(request, 'myApp/home.html')
def about(request):
        return render(request, 'myApp/about.html')
def contact(request):
        return render(request, 'myApp/contact.html')
def login(request):
        return render(request, 'users/login.html')
def password(request):
        return render(request, 'myApp/password.html')
def profile(request):
   return render(request, 'users/profile.html') 
def register(request):
        return render(request, 'users/register.html')
def smartphone(request):
        return render(request, 'myApp/smartphone.html')
def smartwatch(request):
        return render(request, 'myApp/smartwatch.html')
def television(request):
        return render(request, 'myApp/television.html')
def product1(request):
        return render(request, 'myApp/product1.html')
def product2(request):
        return render(request, 'myApp/product2.html')
def product3(request):
        return render(request, 'myApp/product3.html')


           


            


       

               
        




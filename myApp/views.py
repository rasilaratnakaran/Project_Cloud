from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user
from .models import enquiry
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import SmartPhones
from .models import SmartWatches
from .models import Televisions

 
from django.template import loader


from .models import Review
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
 
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
        products = SmartPhones.objects.all()
        return render(request, 'myApp/smartphone.html',{'products':products})
def smartwatch(request):
        products = SmartWatches.objects.all()
        return render(request, 'myApp/smartwatch.html',{'products':products})
def television(request):
        products = Televisions.objects.all()
        return render(request, 'myApp/television.html',{'products':products})
def product1(request):
        products = SmartWatches.objects.all()
        return render(request, 'myApp/product1.html',{'products':products})
def product2(request):
        products = SmartPhones.objects.all()
        return render(request, 'myApp/product2.html',{'products':products})

def product3(request):
        products = Televisions.objects.all()
        return render(request, 'myApp/product3.html',{'products':products})

class ReviewView(View):
    def get(self, request):
        reviews = Review.objects.all()
        context = {'reviews': reviews}
        return render(request, 'myApp/review.html', context)

    def post(self, request):
        description = request.POST.get('description')
        user=request.user
        review = Review(description=description, user=user)
        review.save()

        return render(request,'myApp/product1.html')

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'myApp/edit_review.html'
    fields = ['description']

    def get_success_url(self):
        return reverse_lazy('myApp-review')

class DeleteReviewView(View):
    def post(self, request, pk):

        review = Review.objects.get(id=pk)
        review.delete()

        return redirect('/product1')






           


            


       

               
        




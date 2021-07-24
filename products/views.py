from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from products import views

# Create your views here.
def home(request):
    return render(request,'products/home.html')
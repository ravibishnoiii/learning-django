from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello, world! this is homepage") 
   return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html') 

def contact(request):
    return HttpResponse("Hello, world! this is contact page") 
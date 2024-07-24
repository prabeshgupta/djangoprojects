from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #To pass dynamic content in the template file
    return render(request, "home.html",{"name":"Prabesh"})

def result(request):
    age = 2024 - int(request.GET['year'])
    return render(request, 'result.html', {"name":"Prabesh","age":age})
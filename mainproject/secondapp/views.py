from django.shortcuts import render
from .models import Information

def about(request):
    info = Information()
    info.img = 'admin.png'

    return render(request, 'about.html', {"info":info})

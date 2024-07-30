from django.shortcuts import render
from .models import Information, InformationModel

def about(request):
    # Access data from model using basic class
    # info = Information()
    # info.img = 'admin.png'
    # return render(request, 'about.html', {"info":info})

    #Access data from model
    access = InformationModel.objects.all()
    return render(request, 'about.html', {'access': access})


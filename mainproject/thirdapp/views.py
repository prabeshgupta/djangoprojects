from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    User.objects.create_user(first_name= first_name, last_name=last_name,email=email, username=username, password=password)
                    return redirect('/secondapp/about/')
                else:
                    messages.info(request,"Email already used")
                    return redirect('register')
            else:
                messages.info(request,"Username already taken")
                return redirect('register')
        else:
            messages.info(request,"Password Not Matched")
            return redirect('register')
    else:
        return render(request, 'register.html')
        

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username= username, password= password)

        if user is not None:
            login(request,user)
            return redirect('/secondapp/about/')
        else:
            messages.info(request, "Username or Password mismatched")
            return redirect('user_login')
    else:
        return render(request, 'login.html')
    

def user_logout(request):
    logout(request)
    return redirect("/secondapp/about")
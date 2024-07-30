from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
                    print("Email already used")
            else:
                print("Username already taken")
        else:
            print("Password Not Matched")
    else:
        return render(request, 'register.html')
        


from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        birthdate = request.POST['birthdate']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                print("** Username already exists **")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("** Email is already in use **")
                    return redirect('register')
                else:
                    # looks good!
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    profile = Profile(user_id=user.id, birthdate=birthdate)
                    profile.save()
                    print("** Successfully registered! **")
                    return redirect('login')
        else:
            print('Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("** You are logged in. **")
            return redirect('index')
        else:
            print("** Invalid credentials **")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        print('You are now logged out')
        return redirect('login')

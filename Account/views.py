from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import path

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Account:login')
        else:
            # Add error handling
            print(form.errors)
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Logged in user: {user}")
                login(request, user)
                return redirect('cateringAPP:index_url')
            else:
                print("Invalid login credentials")
                context = {'form': form, 'error': 'Invalid login credentials'}
                return render(request, 'login.html', context)
    else:
        form = AuthenticationForm()
        print("Rendering login form")
    return render(request, 'login.html', {'form': form})

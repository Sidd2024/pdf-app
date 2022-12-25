from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from .forms import *
from .models import *


def index(request):
    return render(request, "pdfScan/index.html")

def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_pass = form.cleaned_data['confirm_pass']
            if password != confirm_pass:
                return render(request, "pdfScan/signup.html", {
                    "form": form,
                    "error": "Passwords didn't match!"
                })
            try:
                user = User.objects.create_user(username, email, password)
                user.save
            except IntegrityError:
                return render(request, "pdfScan/signup.html", {
                    "form": form,
                    "error": "Username already taken!"
                })
            login(request, user)
            return redirect('index')
    else:
        form = signup_form()
        return render(request, "pdfScan/signup.html", {
            "form": form
        })

def signin(request):
    if request.method == 'POST':
        form = signin_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, "pdfScan/signin.html", {
                    "form": form,
                    "error": "Invalid username or password!"
                })
    else:
        form = signin_form()
        return render(request, "pdfScan/signin.html", {
            "form": form
        })

def signout(request):
    logout(request)
    return redirect('index')

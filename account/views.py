from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):
    user=request.user
    if user.is_authenticated:
        return redirect (reverse("app:home"))
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        comfirm_password = request.POST.get("cpassword")
        if not username or not email or not password or not comfirm_password:
            messages.error(request, "Incomplete Details")
            return render (request, "account/signup.html")
        if len(password)<8:
            messages.error(request, "Password Too Short")
            return render (request, "account/signup.html")
        if password != comfirm_password:
            messages.error(request, "Password Didnt Match")
            return render (request, "account/signup.html")
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username Already Exists")
            return render (request, "account/signup.html")
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email Already Exists")
            return render (request, "account/signup.html")
        account = User.objects.create(username = username, email = email)
        account.set_password(password)
        account.save()
        messages.success(request, "Account created successfully")
        return redirect (reverse("app:home"))
    return render (request, "account/signup.html")
def login(request):
    user=request.user
    if user.is_authenticated:
        return redirect (reverse("app:home"))
    if request.method == "POST":
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        if not username or not password:
            messages.error(request, "Incomplete Details")
            return render (request, "account/login.html")
        account = auth.authenticate(username=username, password=password)
        if not account:
            messages.error(request, "Invalid login Details")
            return render (request, "account/login.html")
        
        auth.login(request, account)
        messages.success(request, "Login successfully")
        return redirect (reverse("app:home"))

    return render (request, "account/login.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse("account:login"))
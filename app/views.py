from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'app/home.html')
@login_required
def profile(request):
    return redirect (reverse("app:home"))
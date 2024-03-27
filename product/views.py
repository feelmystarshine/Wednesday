from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.models import Product
# Create your views here.


@login_required
def items(request):
    all_products = Product.objects.all().order_by('-created_at')
    context = {"products" :all_products}
    return render(request, "product/index.html", context)

@login_required
def check(request, id):
    item = Product.objects.filter(id = id).first()
    if not item:
        return redirect((reverse("product:items")))
    context = {"product": item}
    return render (request, "product/check.html", context)

@login_required
def buy(request, id):
    buy = Product.objects.filter(id = id).first()
    if not buy:
        return redirect((reverse("product:items")))
    context = {"product": buy}
    return render (request, "product/buy.html", context)

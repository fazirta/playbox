from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product


def landing(request):
    products = Product.objects.all()

    context = {
        "npm": "2306274983",
        "name": "Muhammad Fazil Tirtana",
        "class": "PBP D",
        "products": products,
    }

    return render(request, "landing/index.html", context)


def create(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:landing")

    context = {
        "npm": "2306274983",
        "name": "Muhammad Fazil Tirtana",
        "class": "PBP D",
        "form": form,
    }

    return render(request, "create/index.html", context)

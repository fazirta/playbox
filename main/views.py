from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
import datetime


def landing(request):
    return render(request, "landing/index.html", {"products": Product.objects.all()})


@login_required(login_url="/signin")
def create(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("main:landing")
    return render(request, "create/index.html", {"form": form})


@login_required(login_url="/signin")
def edit(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, request.FILES, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:profile"))
    context = {"form": form}
    return render(request, "edit/index.html", context)


@login_required(login_url="/signin")
def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:profile"))


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


@login_required(login_url="/signin")
def profile(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "profile/index.html", {"products": products})


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:signin")
    return render(request, "signup/index.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:landing"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, "signin/index.html", {"form": form})


def signout(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:landing"))
    response.delete_cookie("last_login")
    return response

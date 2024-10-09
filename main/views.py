from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
import datetime


def landing(request):
    return render(request, "landing/index.html", {"products": Product.objects.all()})


@csrf_exempt
@require_POST
def create_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    image = request.FILES.get("image")
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        image=image,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


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
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(request):
    data = Product.objects.filter(user=request.user)
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

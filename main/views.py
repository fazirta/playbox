from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers


def landing(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "landing/index.html", context)


def create(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('main:landing')

    context = {"form": form}

    return render(request, "create/index.html", context)


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

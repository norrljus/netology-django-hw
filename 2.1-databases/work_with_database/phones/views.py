from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    template = "catalog.html"
    order_by = request.GET.get("order_by", "name")
    phones = Phone.objects.order_by(order_by)
    context = {"phones": phones, "order_by": order_by}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = "product.html"
    context = {"phone": phone}
    return render(request, template, context)

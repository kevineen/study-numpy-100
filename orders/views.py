from django.shortcuts import render
from django.views.generic import ListView

from .models import Order


def index(request):

    template_name = "orders/index.html"

    return render(request, template_name,)


def list_view(request):
    template_name = "orders/order_list.html"

    return render(request, template_name,)

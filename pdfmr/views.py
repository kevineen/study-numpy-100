from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):

    template_name = "index.html"

    param = {
        "app": "pdfmr",
    }

    return render(request, template_name, param)

from django.urls import path, include

from . import views

app_name = "pdfmr"

urlpatterns = [
    path("", views.index, name="index"),
]

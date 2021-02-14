from django.urls import path

# from .views import OrderListView

from . import views

app_name = "orders"

params = {
    # "app": "index",
    # "nbar": "index",
}

urlpatterns = [
    path("", views.index, params),
]

"""beansAf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from employees.schema import schema
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

from byaf import views

# from byaf.views import file_upload_view

# from .views import views

urlpatterns = [
    path("", views.DataView.as_view(), name="index"),
    # path("templates/", views.index, name="index"),
    path("byaf/", include("byaf.urls")),
    path("pdfmr/", include("pdfmr.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("auth/", obtain_auth_token),
    path("acounts/", include("django.contrib.auth.urls")),
    path("orders/", include("orders.urls")),
    # path("upload/", file_upload_view, name="upload-view"),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

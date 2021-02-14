from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "byaf"

urlpatterns = [
    path("", views.DataView.as_view(), name="index"),
    # path("ajax/", views.DataView.test_ajax_response),
    # path("deldir/", views.PDFPack.as_view(), name="deldir"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

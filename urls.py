from django.conf.urls import include, url
from django.http import HttpResponse

from app import views

urlpatterns = [
    url(r'^verify', views.verify_receipt),
    url('verify/scum', views.verify_receipt_scum),
    url('verify/jellycuts', views.verify_receipt_jelly),
]


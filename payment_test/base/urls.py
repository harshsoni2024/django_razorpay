
from django.urls import path
from . import views
urlpatterns = [
    path('', views.payment_gateway, name='payment_gateway'),
    path('success', views.payment_success, name='success')
]

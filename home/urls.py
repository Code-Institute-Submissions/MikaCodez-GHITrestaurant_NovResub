from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.menu, 'templates/menu.html', name='menu'),
    path('', views.booking, 'templates/booking.html', name='booking'),
]
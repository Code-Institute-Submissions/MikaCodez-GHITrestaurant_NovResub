from django.urls import path
from . import views

urlpatterns = [
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores
    #path 
    path('<int:year>/<str:month>', views.booking, name="booking" ),
]
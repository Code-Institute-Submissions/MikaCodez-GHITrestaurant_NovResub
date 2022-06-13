from django.urls import path
import views

urlpatterns = [
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores
    # path
    path('<int:year>/<str:month>', views.home(request, year, month), name="booking"),
]
from . import views
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path("", views.ReservationList.as_view(), name="reservation"),
    path('reservation_detail/', views.ReservationList.as_view(), name='reservation_detail'),
    path("publish_reservation", views.CreateReservation.as_view(), name="publish_reservation"),
    path('<pk>/update', views.UpdateReservation.as_view(), name="update_reservation"),
    path('<pk>/delete', views.DeleteReservation.as_view(), name="delete_reservation"),
]

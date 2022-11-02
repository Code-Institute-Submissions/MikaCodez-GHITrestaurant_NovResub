from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, UpdateView, DeleteView
from home.views import PageTitleViewMixin
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages
from django.urls import reverse_lazy


class ReservationList(PageTitleViewMixin, generic.ListView):
    """List view for displaying user Reservations"""

    title = "Reservation"
    template_name = "reservation_detail.html"
    context_object_name = "reservation_list"
    model = Reservation

    queryset = Reservation.objects.filter(approved=True).order_by("created_on")
    paginate_by = 3


class CreateReservation(PageTitleViewMixin, View):
    """Class View to add a new reservation"""

    title = "Create Reservation"
    template_name = "publish_reservation.html"

    def get(self, request):
        context = {"reservation_form": ReservationForm(), "title": "Create Reservation"}
        return render(
            request,
            "publish_reservation.html",
            context,
        )

    def post(self, request):
        """post the new reservation to the database"""

        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.instance.author_id = request.user.id
            reservation_form.save()
        else:
            reservation_form = ReservationForm()
        messages.success(
            request, "Your reservation has been created and is pending approval"
        )
        return redirect("reservation_detail")


class UpdateReservation(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    """Class View to update an existing Reservation"""

    model = Reservation
    template_name = "update_reservation.html"
    title = "Update Reservation"

    fields = ["title", "body"]
    success_url = reverse_lazy("reservation_detail")


class DeleteReservation(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    """Class view to delete a Reservation"""

    model = Reservation
    template_name = "delete_reservation.html"
    title = "Delete Reservation"
    success_url = reverse_lazy("reservation_detail")
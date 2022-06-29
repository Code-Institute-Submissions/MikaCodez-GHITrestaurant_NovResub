from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ("created_on", "author", "approved")
    search_fields = ["title", "author"]
    actions = ["approve_reservation"]

    def approve_reservation(self, request, queryset):
        queryset.update(approved=True)
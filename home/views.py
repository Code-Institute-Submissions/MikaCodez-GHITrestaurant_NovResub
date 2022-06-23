from django.views.generic import TemplateView

# code from https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#django.views.generic.base.TemplateView


class PageTitleViewMixin:
    """Mixin used to dynamically add titles to templates"""

    title = ""

    def get_title(self):
        """Returns a title from the object"""
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        title = self.get_title()

        if not title:
            raise ValueError("Fill in the page title")
        context["title"] = self.get_title()
        return context


class HomeView(PageTitleViewMixin, TemplateView):
    """Homepage view"""

    template_name = "home.html"
    title = "Home"

class BookingsView(PageTitleViewMixin, TemplateView):
    """Displays the Bookings template view"""

    title = "Booking"
    template_name = "booking.html"

class MenuView(PageTitleViewMixin, TemplateView):
    """Menupage view"""

    template_name = "menu.html"
    title = "Menu"

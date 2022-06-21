from django.shortcuts import render



def home(request):
    """ A view to return the home page """

    return render(request, 'templates/home.html')


def menu(request):
    """ A view to return the menu page """

    return render(request, 'templates/menu.html')


def booking(request):
    """ A view to return the booking page """

    return render(request, 'templates/booking.html')
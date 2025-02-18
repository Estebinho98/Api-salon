from django.urls import path
from .views import BookingsView, SingleBookingView

urlpatterns = [
    path('bookings', BookingsView.as_view(), name='Bookings'),
    path('bookings/<int:pk>', SingleBookingView.as_view(), name='Detail-Booking'),

]
from django.urls import path
from .views import (
    ReservationCreateView, ReservationDetailView, UserReservationsView,
    UpdateReservationStatusView, DeleteReservationView
)

urlpatterns = [
    path('', ReservationCreateView.as_view(), name='reservation-create'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('user/<int:user_id>/', UserReservationsView.as_view(), name='user-reservations'),
    path('<int:pk>/update/', UpdateReservationStatusView.as_view(), name='update-reservation'),
    path('<int:pk>/delete/', DeleteReservationView.as_view(), name='delete-reservation'),
]

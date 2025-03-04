from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer
from django.shortcuts import get_object_or_404

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        user = self.request.user
        date = serializer.validated_data['date']
        if Reservation.objects.filter(user=user, date=date).exists():
            return Response({"error": "У вас уже есть бронь на этот день"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user)

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserReservationsView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Reservation.objects.filter(user_id=user_id)

class UpdateReservationStatusView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class DeleteReservationView(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

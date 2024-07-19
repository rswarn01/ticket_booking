from rest_framework import generics, permissions, serializers
from .models import Bus, BlockedSeat, Booking
from booking_portal.models import BlockHistory, BookingHistory, SearchHistory
from .serializers import BusSerializer, BlockSeatSerializer, BookingSerializer
from rest_framework.response import Response
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BusSearchView(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        date = self.request.query_params.get("date")

        # Log search history
        if self.request.user.is_authenticated:
            SearchHistory.objects.create(
                user=self.request.user,
                source=source,
                destination=destination,
                search_time=date,
            )

        if source and destination:
            return Bus.objects.filter(source=source, destination=destination)
        return super().get_queryset()


class BlockSeatView(generics.CreateAPIView):
    queryset = BlockedSeat.objects.all()
    serializer_class = BlockSeatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        blocked_seat = serializer.save()

        # Log block seat history
        if self.request.user.is_authenticated:
            BlockHistory.objects.create(
                user=self.request.user,
                bus=blocked_seat.bus,  # Assuming BlockedSeat has a foreign key to Bus
                block_time=blocked_seat.blocked_at,  # or set this manually if needed
            )


class BookTicketView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the booking instance first
        booking = serializer.save(user=self.request.user)

        # Use a transaction to ensure atomicity
        with transaction.atomic():
            blocked_seat = booking.blocked_seat
            bus = blocked_seat.bus  # Access the Bus via BlockedSeat

            # Check if there are enough seats available
            if bus.seats_available <= 0:
                # Raise a validation error if no seats are available
                raise serializers.ValidationError("No seats available on this bus.")

            # Reduce the number of available seats
            bus.seats_available -= 1
            bus.save()

            # Log booking history
            BookingHistory.objects.create(user=self.request.user, booking=booking)

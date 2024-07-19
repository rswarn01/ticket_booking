from rest_framework import serializers
from .models import Bus, BlockedSeat, Booking


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = [
            "id",
            "name",
            "source",
            "destination",
            "start_time",
            "seats_available",
            "stops",
        ]


class BlockSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedSeat
        fields = ["id", "bus", "seat_number", "pickup_point", "blocked_at"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "blocked_seat", "booked_at", "user"]
        extra_kwargs = {"user": {"read_only": True}}

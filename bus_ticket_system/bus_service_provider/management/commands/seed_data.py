from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from bus_service_provider.models import Bus, BlockedSeat, Booking
from booking_portal.models import SearchHistory, BlockHistory, BookingHistory


class Command(BaseCommand):
    help = "Seed database with initial data"

    def handle(self, *args, **kwargs):
        self.seed_users()
        self.seed_buses()
        self.stdout.write(self.style.SUCCESS("Database has been seeded."))

    def seed_users(self):
        User = get_user_model()
        if not User.objects.filter(username="testuser").exists():
            User.objects.create_user(
                username="testuser",
                email="testuser@example.com",
                password="password123",
                phone_number="123456780",
                address="123 Test St",
            )

    def seed_buses(self):
        Bus.objects.bulk_create(
            [
                Bus(
                    name="Bus 101",
                    source="City A",
                    destination="City B",
                    start_time="2024-07-20T10:00:00Z",
                    seats_available=20,
                    stops='["Stop 1", "Stop 2", "Stop 3"]',
                ),
                Bus(
                    name="Bus 102",
                    source="City A",
                    destination="City C",
                    start_time="2024-07-21T12:00:00Z",
                    seats_available=30,
                    stops='["Stop 4", "Stop 5", "Stop 6"]',
                ),
            ]
        )

        # Optionally, create some blocked seats
        BlockedSeat.objects.bulk_create(
            [
                BlockedSeat(bus_id=1, seat_number=1, pickup_point="Stop 1"),
                BlockedSeat(bus_id=1, seat_number=2, pickup_point="Stop 2"),
            ]
        )

        # Optionally, create some bookings
        user = get_user_model().objects.get(username="testuser")
        Booking.objects.bulk_create(
            [
                Booking(blocked_seat_id=1, user=user),
                Booking(blocked_seat_id=2, user=user),
            ]
        )

        # Optionally, create search, block and booking histories
        SearchHistory.objects.create(user=user, source="City A", destination="City B")
        BlockHistory.objects.create(user=user, bus_id=1)
        BookingHistory.objects.create(user=user, booking_id=1)

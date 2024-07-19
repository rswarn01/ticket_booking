from django.db import models


class Bus(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    seats_available = models.IntegerField()
    stops = models.TextField()  # List of stops as a JSON string

    def __str__(self):
        return self.name


class BlockedSeat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    pickup_point = models.CharField(max_length=100)
    blocked_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    blocked_seat = models.ForeignKey(BlockedSeat, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

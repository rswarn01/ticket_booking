from django.db import models
from django.contrib.auth import get_user_model


class SearchHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)


class BlockHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bus = models.ForeignKey("bus_service_provider.Bus", on_delete=models.CASCADE)
    block_time = models.DateTimeField(auto_now_add=True)


class BookingHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    booking = models.ForeignKey(
        "bus_service_provider.Booking", on_delete=models.CASCADE
    )
    booking_time = models.DateTimeField(auto_now_add=True)

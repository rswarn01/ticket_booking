from rest_framework import serializers
from .models import SearchHistory, BlockHistory, BookingHistory


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ["id", "user", "source", "destination", "search_time"]


class BlockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockHistory
        fields = ["id", "user", "bus", "block_time"]


class BookingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingHistory
        fields = ["id", "user", "booking", "booking_time"]

from rest_framework import generics, permissions
from .models import SearchHistory, BlockHistory, BookingHistory
from .serializers import (
    SearchHistorySerializer,
    BlockHistorySerializer,
    BookingHistorySerializer,
)


class SearchHistoryView(generics.ListCreateAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]


class BlockHistoryView(generics.ListCreateAPIView):
    queryset = BlockHistory.objects.all()
    serializer_class = BlockHistorySerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingHistoryView(generics.ListCreateAPIView):
    queryset = BookingHistory.objects.all()
    serializer_class = BookingHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

from django.urls import path
from .views import SearchHistoryView, BlockHistoryView, BookingHistoryView

urlpatterns = [
    path("search-history/", SearchHistoryView.as_view(), name="search_history"),
    path("block-history/", BlockHistoryView.as_view(), name="block_history"),
    path("booking-history/", BookingHistoryView.as_view(), name="booking_history"),
]

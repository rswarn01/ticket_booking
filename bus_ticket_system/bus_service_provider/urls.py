from django.urls import path
from .views import BusSearchView, BlockSeatView, BookTicketView

urlpatterns = [
    path("search/", BusSearchView.as_view(), name="bus_search"),
    path("block-seat/", BlockSeatView.as_view(), name="block_seat"),
    path("book-ticket/", BookTicketView.as_view(), name="book_ticket"),
]

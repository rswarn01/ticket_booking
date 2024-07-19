# Bus Ticket Booking System
# Project Overview
The Bus Ticket Booking System is a web application that allows users to search for buses, block seats, and book tickets. It consists of two primary components: the Bus Ticket Service Provider API and the Bus Ticket Booking Portal API. The system is built using Django REST Framework and includes interactive Swagger documentation for easy exploration of API endpoints.

**Features**
# Bus Ticket Service Provider
1. Bus Search: Search for buses based on source, destination, and date of journey.
2. Block Seats: Block seats on a bus for a specified pickup point.
3. Book Tickets: Book tickets based on a blocked seat ID.
   
# Bus Ticket Booking Portal
1. User Registration: Register new users.
2. User Login: Authenticate users to access the system.
3. Search History: Maintain a history of all search queries.
4. Blocking History: Maintain a history of all seat blockings.
5. Booking History: Maintain a history of all bookings.
    
**API Documentation**
Interactive API documentation is available via Swagger UI at /swagger/.

# API Endpoints
**Bus Ticket Service Provider API**

# User Registration
Endpoint: POST /api/register/
Description: Register a new user.

Request Body:
first_name: User's first name
last_name: User's last name
email: User's email
phone_number: User's phone number
address: User's address

   
# Login
Endpoint: POST /api/token/
Description: Log in an existing user.
Request Body:
email: User's email
password: User's password


# Bus Search
Endpoint: GET /api/bus-service/search/
Description: Search for buses based on source, destination, and date of journey.
Parameters:
source: Source location (query parameter)
destination: Destination location (query parameter)
date: Date of journey (query parameter)


# Block Seat
Endpoint: POST /api/bus-service/block-seat/
Description: Block seats on a bus.
Request Body:
bus: ID of the bus (foreign key)
seat_number: Number of the seat
pickup_point: Pickup location


# Book Ticket
Endpoint: POST /api/bus-service/book-ticket/
Description: Book tickets based on a blocked seat ID.
Request Body:
blocked_seat: ID of the blocked seat (foreign key)


# Bus Ticket Booking Portal API
# Search History
Endpoint: GET /api/booking-portal/search-history/
Description: Retrieve the history of all search queries made by the user.


# Block History
Endpoint: GET /api/booking-portal/block-history/
Description: Retrieve the history of all seat blockings made by the user.


# Booking History
Endpoint: GET /api/booking-portal/booking-history/
Description: Retrieve the history of all bookings made by the user.


# Setup and Installation
# Clone the Repository:
1. git clone https://github.com/rswarn01/ticket_booking
2. cd bus_ticket_system

# Install Dependencies:
pip install -r requirements.txt

# Apply Migrations:
python manage.py migrate

# Run the Development Server:
python manage.py runserver

# Access the API Documentation:
Open your browser and navigate to http://localhost:8000/swagger/ to view the interactive API documentation.

Feel free to adjust any sections according to the specifics of your project and any additional details you may want to include

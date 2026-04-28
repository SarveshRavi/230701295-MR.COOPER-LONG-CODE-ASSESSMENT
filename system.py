from models import Booking
from data import rooms

class HotelSystem:
    def __init__(self):
        self.bookings = []
        self.booking_count = 1 
    def check_availability(self, room_type):
        available = [room for room in rooms if room.room_type == room_type and room.is_available]
        return available
    def create_booking(self, guest, room, checkin, checkout):
        booking = Booking(self.booking_count, guest, room, checkin, checkout)
        self.booking_count += 1
        room.is_available = False
        self.bookings.append(booking)
        return booking  
    def make_payment(self, booking):
        booking.paid = True
    def checkin(self, booking):
        print(f"Room {booking.room.room_id} is now OCCUPIED")
    def checkout(self, booking):
        booking.room.is_available = True
        print(f"Checkout complete. Final bill: ₹{(booking.room.price)}")
      

    


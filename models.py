class Guest:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        pass
class Room:
    def __init__(self,room_id, room_type, price):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.is_available = True
        pass    
class Booking:
    def __init__(self,booking_id, guest, room, checkin, checkout):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.checkin = checkin
        self.checkout = checkout
        self.paid = False
        pass  

    

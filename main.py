from system import HotelSystem
from models import Guest
def main():
    system = HotelSystem()
    print("HOTEL BOOKING SYSTEM")
    name = input("Enter guest name: ")
    phone = input("Enter Phone ")
    guest = Guest(name)
    checkin = input("Enter check-in date: ")
    checkout = input("Enter check-out date: ")
    room_type = input("Enter room type (Single/Double/Suite/Queen/King): ")
    available_rooms = system.check_availability(room_type)
    if not available_rooms:
        print("No rooms available!")
        return
    print("\nAvailable Rooms:")
    for i, room in enumerate(available_rooms):
        print(f"{i+1}. Room {room.room_id} - ₹{room.price}")
    choice = int(input("Select room: "))-1
    selected_room = available_rooms[choice]
    booking = system.create_booking(guest, selected_room, checkin, checkout)
    print(f"\nBooking created!ID: {booking.booking_id}")
    pay = input("Pay now? (yes/no): ")
    if pay.lower() == "no":
        print("Booking CAncel")
        exit 
    elif pay.lower() == "yes":
        system.make_payment(booking)
        print("Payment success")      
        print("\nCHECKIN")
        system.checkin(booking)
        print("\nCHECKOUT")
        system.checkout(booking)
    else:
        print("PLease select yes/no")    
if __name__ == "__main__":
    main()        



































#Post conditions- Booking record created.Room status updated Invoice generated on checkout.NoNFUNCTIONAL- AVailability check must be real time. Booking confirmation sent within 5s.System must prevent double booking via transactional locking    
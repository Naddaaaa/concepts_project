from datetime import datetime

class Reservation:
    def __init__(self, db, room_manager):
        self.db = db
        self.room_manager = room_manager

    def make_reservation(self, customer_name, room_number, check_in_date, check_out_date):
        if self.room_manager.check_availability(room_number):
            query = """
                INSERT INTO reservations (customerName, roomNumber, checkInDate, checkOutDate)
                VALUES (?, ?, ?, ?)
            """
            self.db.execute_query(query, (customer_name, room_number, check_in_date, check_out_date))
            self.room_manager.book_room(room_number)
            print(f"Reservation for {customer_name} in room {room_number} from {check_in_date} to {check_out_date} confirmed.")
        else:
            print(f"Room {room_number} is not available for reservation.")

    
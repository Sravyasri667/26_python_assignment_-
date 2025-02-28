
class FlightTicket:
    def __init__(self, flight_number,
    airline,from_city, to_city, 
    date, passengers, 
    class_type, 
    price, booking_id,
    departure_time, arrival_time,
    traveler_names):
        self.flight_number = flight_number
        self.airline = airline
        self.from_city = from_city
        self.to_city = to_city
        self.date = date
        self.passengers = passengers
        self.class_type = class_type
        self.price = price
        self.booking_id = booking_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.traveler_names = traveler_names

    def display_ticket(self):
        print("--- Flight Ticket ---")
        print(f"Booking ID: {self.booking_id}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")
        print(f"From: {self.from_city}")
        print(f"To: {self.to_city}")
        print(f"Date: {self.date.strftime('%Y-%m-%d')}")
        print(f"Departure Time: {self.departure_time.strftime('%H:%M')}")
        print(f"Arrival Time: {self.arrival_time.strftime('%H:%M')}")
        print(f"Passengers: {self.passengers}")
        print(f"Class: {self.class_type}")
        print(f"Price: ₹{self.price:.2f}")
        print("Traveler Names:")
        for name in self.traveler_names:
            print(f"  - {name}")
        print("--------------------")

def generate_booking_id():
    return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))

def get_time_input(prompt):
    while True:
        try:
            time_str = input(prompt)
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            print("Invalid time format. Use HH:MM.")

def book_flight():
    try:
        flight_number = input("Enter Flight Number: ")
        airline = input("Enter Airline: ")
        from_city = input("Enter From City: ")
        to_city = input("Enter To City: ")

        while True:
            try:
                date_str = input("Enter Date (YYYY-MM-DD): ")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please useтрибу-MM-DD.")

        passengers = int(input("Enter Number of Passengers: "))
        class_type = input("Enter Class (e.g., Economy, Business, First): ")
        price = float(input("Enter Price: "))

        departure_time = get_time_input("Enter Departure Time (HH:MM): ")
        arrival_time = get_time_input("Enter Arrival Time (HH:MM): ")

        traveler_names = []
        for i in range(passengers):
            traveler_names.append(input(f"Enter Name of Passenger {i + 1}: "))

        booking_id = generate_booking_id()

        ticket = FlightTicket(flight_number, airline, from_city, to_city, date, passengers, class_type, price, booking_id, departure_time, arrival_time, traveler_names)
        return ticket

    except ValueError:
        print("Invalid input. Please enter valid values.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Welcome to Flight Booking System!")
    booked_ticket = book_flight()

    if booked_ticket:
        print("\nBooking successful!")
        booked_ticket.display_ticket()
    else:
        print("\nBooking failed.")

if __name__ == "__main__":
    main()

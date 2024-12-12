import datetime


class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, total_seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.booked_seats = 0

    def calculate_voyage_duration(self):
        return self.arrival_time - self.departure_time

    def has_available_seats(self):
        return self.booked_seats < self.total_seats

class Trip:
    def __init__(self, route, start_time, end_time, total_seats):
        self.route = route
        self.start_time = start_time
        self.end_time = end_time
        self.total_seats = total_seats
        self.booked_seats = 0

    def add_route(self):
        cities = self.route.split(", ")
        formatted_route = " ---> ".join(cities)
        return f"Маршрут: {formatted_route}"

    def calculate_trip_duration(self):
        return self.end_time - self.start_time

    def has_available_seats(self):
        return self.booked_seats < self.total_seats

    def book_seat(self):
        if self.has_available_seats():
            self.booked_seats += 1
            return 'Бронирование одобрено'
        else:
            return 'Бронирование не одобрено: нет свободных мест'


flight = Flight(
    flight_number="A123",
    departure_city="Bishkek",
    arrival_city="Moscow",
    departure_time=datetime.datetime(2024, 12, 12, 10, 30),
    arrival_time=datetime.datetime(2024, 12, 12, 12, 0),
    total_seats=3
)

trip = Trip(
    route="Bishkek, Moscow, Paris",
    start_time=datetime.datetime(2024, 12, 12, 8, 0),
    end_time=datetime.datetime(2024, 12, 12, 20, 0),
    total_seats=2
)

print(f"Рейс: {flight.flight_number} из {flight.departure_city} в {flight.arrival_city}")
print(f"Длительность рейса: {flight.calculate_voyage_duration()}")

print(trip.add_route())
print(f"Длительность поездки: {trip.calculate_trip_duration()}")

print(trip.book_seat())
print(trip.book_seat())
print(trip.book_seat())

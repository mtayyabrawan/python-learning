"""
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
"""


from random import randint


class Train:
    def __init__(self, name, fare=500, seats=1000):
        self.name = name
        self.fare = fare
        self.seats = seats
        pass

    def book(self, fro, to, name):
        self.seats -= 1
        print(
            f"Seat No {randint(1000, 1000000)} of train {self.name} is now reserved for {name} from {fro} to {to}")

    def get_status(self):
        print(
            f"Currently {self.name} is running & total {self.seats} seats are available now for booking")

    def get_fare(self):
        print(f"Fare of {self.name} is Rs.{self.fare}")


train_1 = Train("Tezgaam")

train_1.book("Rawalpindi", "Lahore", "Muhammad Tayyab")
train_1.get_status()
train_1.get_fare()

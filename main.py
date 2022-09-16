import random


destinations = ["Egypt", "Amsterdam", "Nairobi","Abu Dabi" ]
resturants = ["Papadeaeuxs", "Lucas", "Grant Steakhouse", "Grillers"]
transportations = ["Scooter", "Motorcycle", "Taxi", "Uber"]
excursions = ["Zoo", "Aquarium", "Mountain Climbing", "Museum"]

def random_destination():
    print("Destination: " + random.choice(destinations))

def random_resturant():
    print("Resturant: " + random.choice(resturants))

def random_transportation():
    print("Transportation: " + random.choice(transportations))


def random_excursion():
    print("Excursion: " + random.choice(excursions))

def day_trip_Question():
    random_destination()
    random_resturant()
    random_transportation()
    random_excursion()

day_trip = day_trip_Question()

def satisfied_with_trip():
    satisfied = input("Do you like the trip we have planned? Yes or No? ")
    if satisfied == "Yes":
        print(day_trip)
    else:
        day_trip_Question()
        satisfied_with_trip()

satisfied_with_trip()
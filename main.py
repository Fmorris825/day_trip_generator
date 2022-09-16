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

def satisfied_with_trip():
    satisfied = input("Do you like the trip we have planned? Yes or No?")

def run():
    random_destination()
    random_resturant()
    random_transportation()
    random_excursion()
    satisfied_with_trip()

day_trip = run()


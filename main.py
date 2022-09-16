import random

destinations = ["Egypt", "Amsterdam", "Nairobi","Abu Dabi" ]
resturants = ["Papadeaeuxs", "Lucas", "Grant Steakhouse", "Grillers"]
transportations = ["Scooter", "Motorcycle", "Taxi", "Uber"]
excursions = ["Zoo", "Aquarium", "Mountain Climbing", "Museum"]

def random_destination():
    print(random.choice(destinations))

def random_resturant():
    print(random.choice(resturants))

def random_transportation():
    print(random.choice(transportations))

def random_excursion():
    print(random.choice(excursions))

def run():
    random_destination()
    random_resturant()
    random_transportation()
    random_excursion()




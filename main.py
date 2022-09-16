import random


destinations = ["Egypt", "Amsterdam", "Nairobi","Abu Dabi" ]
resturants = ["Papadeaeuxs", "Lucas", "Grant Steakhouse", "Grillers"]
transportations = ["Scooter", "Motorcycle", "Taxi", "Uber"]
excursions = ["Zoo", "Aquarium", "Mountain Climbing", "Museum"]

def random_destination():
    Destination = "Destination: " + random.choice(destinations)
    print(Destination)
    return Destination

def random_resturant():
    Resturant = "Resturant: " + random.choice(resturants)
    print(Resturant)
    return Resturant

def random_transportation():
    Transportation = "Transportation: " + random.choice(transportations)
    print(Transportation)
    return Transportation

def random_excursion():
    Excursion = "Excursion: " + random.choice(excursions)
    print(Excursion)
    return Excursion

def day_trip_Question():
    random_destination()
    random_resturant()
    random_transportation()
    random_excursion()
    return [random_destination(), random_resturant(), random_transportation(), random_excursion()]

d1 = random_destination()
r1 = random_resturant()
t1 =  random_transportation()
e1 = random_excursion()
day_trip = d1, r1, t1, e1

def satisfied_with_trip():
    satisfied = input("Do you like the trip we have planned? Yes or No? ")
    if satisfied == "Yes":
        print(day_trip)
    else:
        day_trip_Question()
        satisfied_with_trip()

satisfied_with_trip()
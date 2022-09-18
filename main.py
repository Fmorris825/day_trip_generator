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
    Destination = random_destination()
    Resturant = random_resturant()
    Transportation = random_transportation()
    Excursion = random_excursion()
    return [Destination, Resturant, Transportation, Excursion]
    
Destination = random_destination()
Resturant = random_resturant()
Transportation =  random_transportation()
Excursion = random_excursion()
day_trip = [Destination, Resturant, Transportation, Excursion]

def confirm_trip():
    confirmation = input("Please type 'Confirm' if the trip looks complete. ")
    if confirmation == "Confirm":
        print([random_destination(),random_resturant(),random_transportation(),random_excursion()] + [ 'Completed!'])

def satisfied_with_trip():

    satisfied = input("Do you like the trip we have planned? Yes or No? ")
    if satisfied == "Yes":
        print(random_destination(),random_resturant(),random_transportation(),random_excursion())
        confirm_trip()
    else:
        random_destination()
        random_resturant()
        random_transportation()
        random_excursion()
        satisfied_with_trip()

satisfied_with_trip()


import random
from tabnanny import check


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
    

day_trip = day_trip_Question()
print(day_trip)

def confirm_trip():
    confirmation = input("Please type 'Confirm' if the trip looks complete. ")
    confirmation2 = input("Would you like to Rerun the Day trip Generation or Confirm trip itnerary? Please Enter 'Confirm' or 'Rerun'. ")
    if confirmation == "Confirm":
        print(day_trip + [ 'Completed!'])
    if confirmation2 == "Rerun":
        rerun = day_trip_Question()
        satisfied = input("Do you like the trip we have planned? Yes or No? ")
        if satisfied == "Yes":
            print(rerun)
            confirmation = input("Please type 'Confirm' if the trip looks complete. ")
            if confirmation == "Confirm":
                print(rerun + [ 'Completed!'])
    else:
        confirm_trip()


def satisfied_with_trip():
    satisfied = input("Do you like the trip we have planned? Yes or No? ")
    if satisfied == "Yes":
        print(day_trip)
    else:
        rerun = day_trip_Question()
        satisfied = input("Do you like the trip we have planned? Yes or No? ")
        if satisfied == "Yes":
            print(rerun)
            confirmation = input("Please type 'Confirm' if the trip looks complete. ")
            if confirmation == "Confirm":
                print(rerun + [ 'Completed!'])
        
        
  
satisfied_with_trip()
confirm_trip()

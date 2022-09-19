import random

destinations = ["Egypt", "Amsterdam", "Nairobi","Abu Dabi" ]
resturants = ["Papadeaeuxs", "Lucas", "Grant Steakhouse", "Grillers"]
transportations = ["Scooter", "Motorcycle", "Taxi", "Uber"]
excursions = ["Zoo", "Aquarium", "Mountain Climbing", "Museum"]

def get_random_destination():
    Destination = "Destination: " + random.choice(destinations)
    print(Destination)
    return Destination

def get_random_resturant():
    Resturant = "Resturant: " + random.choice(resturants)
    print(Resturant)
    return Resturant

def get_random_transportation():
    Transportation = "Transportation: " + random.choice(transportations)
    print(Transportation)
    return Transportation

def get_random_excursion():
    Excursion = "Excursion: " + random.choice(excursions)
    print(Excursion)
    return Excursion

def get_trip_itenerary():
    Destination = get_random_destination()
    Resturant = get_random_resturant()
    Transportation = get_random_transportation()
    Excursion = get_random_excursion()
    return [Destination, Resturant, Transportation, Excursion]
    

day_trip = get_trip_itenerary()

def confirm_trip():
    confirmation = input("Would you like to Rerun the Day trip generator or Confirm your trip itnerary? Please Enter 'Confirm' or 'Rerun'. ")
    if confirmation == "Confirm":
        print(day_trip + [ 'Completed!'])
    elif confirmation == "Rerun":
        rerun = get_trip_itenerary()
        satisfied = input("Do you like the trip itenerary we have planned for you? Please enter 'Yes' or 'No'? ")
        if satisfied == "Yes":
            print(rerun)
            confirmation = input("Please type 'Confirm' if the trip itnerary to complete your tripl planning. ")
            if confirmation == "Confirm":
                print(rerun + [ 'Completed!'])
    else:
        confirm_trip()


def get_satisfaction_confirmatino():
    satisfied = input("Do you like the trip we have planned? Yes or No? ")
    if satisfied == "Yes":
        print(day_trip)
    else:
        rerun = get_trip_itenerary()
        satisfied = input("Do you like the trip we have planned? Yes or No? ")
        if satisfied == "Yes":
            print(rerun)
            confirmation = input("Please type 'Confirm' if the trip looks complete. ")
            if confirmation == "Confirm":
                print(rerun + [ 'Completed!'])
        
        
  
get_satisfaction_confirmatino()
confirm_trip()

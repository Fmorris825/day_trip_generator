import random


def day_trip_options():
    destinations = ["Egypt", "Amsterdam", "Nairobi","Abu Dabi" ]
    resturants = ["Papadeaeuxs", "Lucas", "Grant Steakhouse", "Grillers"]
    transportations = ["Scooter", "Motorcycle", "Taxi", "Uber"]
    excursions = ["Zoo", "Aquarium", "Mountain Climbing", "Museum"]

    Destination = "Destination: " + random.choice(destinations)
    Resturant = "Resturant: " + random.choice(resturants)
    Transportation = "Transportation: " + random.choice(transportations)
    Excursion = "Excursion: " + random.choice(excursions)

    return [Destination, Resturant, Transportation, Excursion]


satisfaction_prompt = "Do you like the trip we have planned? Please type 'Yes' or 'No'? "
confirmation_prompt = "If you wish to accept this trip Itnerary, Please type 'Confirm'. If you wish to rerun the Day Trip Generator please input 'Rerun'.  "

def display_day_trip_itinerary(options):
    for option in (options):
        print(option)

def get_user_satisfaction(options):
    user_satisfaction_level = input(satisfaction_prompt)
    if user_satisfaction_level == "Yes":
        print(options)
    elif user_satisfaction_level == "No":
        run()
    else:
        get_user_satisfaction(options)

def confirm_trip_itinerary(options):
    user_confirmation = input(confirmation_prompt)
    if user_confirmation == "Confirm":
        print(f'{options} Completed Booking! ')
    elif user_confirmation == "Rerun":
        run()
    else:
        confirm_trip_itinerary(options)
    

def run():
    options = day_trip_options()
    display_day_trip_itinerary(options)
    get_user_satisfaction(options)
    confirm_trip_itinerary(options)
    
run()

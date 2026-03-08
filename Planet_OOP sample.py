class Planet:
    def __init__(self, name, gravity):
        self.name = name
        self.gravity = gravity
        
    def calculate_weight(self, earth_weight):
        return earth_weight * self.gravity

# data to pull
planets = {
    1: Planet("Mercury", 0.38),
    2: Planet("Venus", 0.91),
    3: Planet("Mars", 0.38),
    4: Planet("Jupiter", 2.53),
    5: Planet("Saturn", 1.07),
    6: Planet("Uranus", 0.89),
    7: Planet("Neptune", 1.14)
}

print("Welcome to simple weight calculator in each planet of Solar system")
print("Here's the list of planet and their number for your reference:")
for i, planet in planets.items(): #for loop to gain access on planets dictionary, n for numbers and i for object
    print(f"{i}: {planet.name}") #using f string for short and yet clean command calling 2 variables (i and planet)
    
while True:

#user's input
    try:
        earth_weight = float(input("What's your weight on Earth (in kg)?: "))
    except ValueError:
        print("Numbers only")
        continue
    planet_input = input("Select planet(s) from 1-7 (comma separated if multiple): ")

#cleaning and convertion of data and try to check if user's input is correct
    planet_numbers = planet_input.split(",")
    try:
        planet_choices = set([int(num.strip()) for num in planet_numbers]) #used 'set' to avoid duplication of result if ever the user puts multiple same planet numbers
    except ValueError:
        print("Please enter only numbers between 1-7 separated by commas.")
        continue

#loop to check if planet number exist in dictionary
    print(f"You are {earth_weight:.2f}kg in Earth")
    for num in sorted(planet_choices):
    # condition if planet number is in dictionary and if YES, it will call Planet class for name of planet, gravity and calculation of weight
        if num in planets:
            planet_obj = planets[num]
            weight_on_planet = planet_obj.calculate_weight(earth_weight)
            print(f"On {planet_obj.name}, your weight is {weight_on_planet:.2f}kg") #:.2f to limit decimal into 2
    # if number does not exist in library
        else:
            print(f"{num} is invalid number")

    ask = input("Please type 'y/Y' if you want to calculate again: ")

    if ask.lower() != 'y':
        break


#for num, planet_obj in planets.items():
#    weight_on_planet = planet_obj.calculate_weight(earth_weight)
#    print(f"On {planet_obj.name} (key {num}), your weight is {weight_on_planet}")

"""
User Input
───────────────
1. Enter Earth weight  → float
2. Enter planet choice(s) → string (e.g., "1,3,5")
─────────────────────────
Process Input
───────────────
3. Split string by commas → list of strings
4. Strip spaces + convert to int → planet_choices (list of integers)
─────────────────────────
Loop Over User Choices
───────────────
5. For each num in planet_choices:
    ├─ Check if num exists in planets dictionary
    │   ├─ Yes → continue
    │   └─ No → print "Invalid number"
    └─ Get Planet object from dictionary:
        planet_obj = planets[num]
─────────────────────────
Calculate Weight
───────────────
6. Call object method:
    weight_on_planet = planet_obj.calculate_weight(earth_weight)
    └─ Inside method:
        self = planet_obj
        self.gravity = planet_obj.gravity
        returns earth_weight * self.gravity
─────────────────────────
Output Result
───────────────
7. Print result:
    On {planet_obj.name} (key {num}), your weight is {weight_on_planet}
─────────────────────────
Repeat loop for all numbers in planet_choices
"""
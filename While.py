planet_name = ""
list_of_planets = []

while planet_name.lower() != "stop":
    if planet_name:
        list_of_planets.append(planet_name)
    planet_name = input("Enter palnet name or stop: ")

for planet, side in list_of_planets:
    print(planet)
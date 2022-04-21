planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0]) # The first planet is Mercury

print( len(planets) ) # 8

planets.append("Pluto") # ...'Neptune','Pluto']
print(planets)

planets.pop() # Delete last element from the list

print (planets.index("Venus")) # 1

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

print( min(gravity_on_planets) ) # 0.377
print( max(gravity_on_planets) ) # 2.36
print( min(gravity_on_planets[3:6]) ) # 0.377

print( planets[3:7]) # ['Mars', 'Jupiter', 'Saturn', 'Uranus'] start from 3 ends before 7
print( planets[3:]) # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets.sort()
print(planets) # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
planets.sort(reverse=True)
print(planets) # ['Venus', 'Uranus', 'Saturn', 'Neptune', 'Mercury', 'Mars', 'Jupiter', 'Earth']
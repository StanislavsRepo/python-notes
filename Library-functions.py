planets = {
    'name':'Earth',
    'moons':1
}

print(planets.get('name')) # Earth
print(planets.get('nameXX')) # None

planets.update({
    'name':'Saturn',
    'moons': 6
})

print(planets) # {'name': 'Saturn', 'moons': 6}

planets['orbital period'] = 7654
print(planets) # {'name': 'Saturn', 'moons': 6, 'orbital period': 7654}

planets.pop('orbital period')
print(planets) # {'name': 'Saturn', 'moons': 6}

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for month in rainfall.keys():
    print(f"{month}: {rainfall[month]}")

# october: 3.5
# november: 4.2
# december: 2.1

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

print(rainfall['december']) # 3.1

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter') # There was 10.8cm in the last quarter
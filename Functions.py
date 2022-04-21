def variable_length(*args):
    print(args)

variable_length(1,2,3) # (1, 2, 3)

def sequence_time(*ar):
    total_time = sum(ar)
    print(total_time)

sequence_time(1,2) # 3

def variable_length(**kwargs):
    print(kwargs)

variable_length(test=4, moons=5, foo=3) # {'test': 4, 'moons': 5, 'foo': 3}

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")

fuel_report(tank1=10,tank_2=30, tank3 = 60)
print("\n")

loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""
parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        print(key + " " + value)
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)
print("\n")

#call error
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print(err)

# There is not enough water for 5 astronauts after 2 days!
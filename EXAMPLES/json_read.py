from dataclasses import dataclass
from pprint import pprint
import json

# json.loads(STRING)     load from string
# json.load(FILE_OBJECT) load from file-like object

@dataclass
class Planet:
    name: str
    moons: list

with open('../DATA/solar.json') as solar_in:  # open JSON file for reading
    solar = json.load(solar_in)  # load from file object and convert to Python data structure
    all_planets = []
    for section, data in solar.items():
        if section.endswith('planets'):
            for planet_data in data:
                moons = planet_data["moons"] if planet_data['moons'] else []
                planet = Planet(planet_data['name'], moons)
                all_planets.append(planet)

for planet in all_planets:
    print(planet.name, planet.moons[:5])


def encode(obj):
    if isinstance(obj, Planet):
        return [obj.name, obj.moons]
    else:
        return obj

planets = json.dumps(all_planets, default=encode)
print(planets)


exit()
# uncomment to see raw Python data
print('-' * 60)
pprint(solar)
print('-' * 60)
print('\n\n')

print(solar['innerplanets'])  # solar is just a Python dictionary
print('*' * 60)
print(solar['innerplanets'][0]['name'])
print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets']:
    print(planet['name'])

print("*" * 60)
for group in solar:
    if group.endswith('planets'):
        for planet in solar[group]:
            print(planet['name'])

cities = {'cs': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}


cities['NY'] = 'New York'
cities['OR'] = 'Portland'

for i in cities:
    print(i)


def find_city(themap, state):
    if state in themap:
        return  themap[state]
    else:
        return "Not found"

#ok pay attention
cities['_find'] = find_city

while True:
    print("State?(ENTER too quit)"),
    state = input(">")
    if not state: break

    #this line is the most important ever!study!
    city_found = cities['_find'](cities, state)
    print(city_found)


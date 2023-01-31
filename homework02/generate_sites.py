import json
import random 

MarsSyrtisMajor = {} # made a dictionary
MarsSyrtisMajor['Meteorite Landing Sites'] = [] # made a key within the dictionary

counter = 1

for i in range(5):
    latitude = random.uniform(16.0, 18.0) # creates a range for both lat and long
    longitude = random.uniform(82.0, 84.0) # allows for the number to be a float
    composition = random.randint(1,3) # allows for random number to be a int

    if (composition == 1):
        compdef = "Stony"
    elif (composition == 2):
        compdef = "Iron"
    else:
        compdef = "Stony-Iron"

    MarsSyrtisMajor['Meteorite Landing Sites'].append({'Site ID':counter, 'Latitude':latitude, 'Longitude':longitude, 'Composition':compdef})
    
    counter += 1

    with open('MarsSyrtisMajor.json', 'w') as out:
            json.dump(MarsSyrtisMajor, out, indent=2)


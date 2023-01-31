import json
import math
mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def calc_time(distance: float) -> float:
    maxSpeed = 10
    totTime = (distance/maxSpeed) 
    return(totTime)

def calc_sampleTime(compdef):
    if (compdef == 'Stony'):
        samptime = 1.0
    elif (compdef == 'Iron'):
        samptime = 2.0
    else:
        samptime = 3.0
    return(samptime)

def main():
    with open('MarsSyrtisMajor.json', 'r') as f:
        syrtis_data = json.load(f)

    currLat = 16.0
    currLong = 82.0
    totalTime = 0.

    for i in range(len(syrtis_data['Meteorite Landing Sites'])):
        sitenumber = syrtis_data['Meteorite Landing Sites'][i]['Site ID']
        legtime = calc_time(calc_gcd(currLat, currLong, syrtis_data['Meteorite Landing Sites'][i]['Latitude'], syrtis_data['Meteorite Landing Sites'][i]['Longitude']))
        sampleTime = calc_sampleTime(syrtis_data['Meteorite Landing Sites'][i]['Composition'])

    #totalTime = legtime + sampleTime
    #currLat = syrtis_data['Meteorite Landing Sites'][i]['Latitude']
    #currLong = syrtis_data['Meteorite Landing Sites'][i]['Longitude']

        print("Leg: " + str(sitenumber) + ", Time Traveled: " + str(legtime) + " hours" + ", Time for sample: " + str(sampleTime) + " hours")
        totalTime += legtime + sampleTime
        currLat = syrtis_data['Meteorite Landing Sites'][i]['Latitude']
        currLong = syrtis_data['Meteorite Landing Sites'][i]['Longitude']
    
    print("~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*~.*")
    print("Total number of sites traveled: " + str(len(syrtis_data['Meteorite Landing Sites'])) + ", Total Trip Time: " + str(totalTime) + " hours")

if __name__ == '__main__':
    main()

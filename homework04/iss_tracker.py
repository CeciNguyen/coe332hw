import requests 
import xmltodict
import math
from flask import Flask, request

app = Flask(__name__)

url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
response = requests.get(url)

data = xmltodict.parse(response.text)

@app.route('/', methods=['GET'])
def dataset():
    """
    This function returns all of the data from the XML file.
    Args:
    This function does not have a set parameter, but the app route can be called 
    with '/' and the route retrieves the data through 'GET'
    Returns:
    This function returns the data set as a dictionary
    """
    return data

@app.route('/epochs', methods=['GET'])
def allepochs():
     """
     This function returns all of the epochs in the data set
     Args:
     This function does not have a set parameter, but the app route can be called 
     with '/epochs' and the route retrieves the data through 'GET'
     Returns:
     This function returns all the epochs (strings) in the ISS data set
     """     
     result = []
     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     for e in range(len(ds_statevector)):         
       result.append(ds_statevector[e]['EPOCH'])
     return result

@app.route('/epochs/<int:epoch>', methods=['GET'])
def spefepochs(epoch):
     """
     This function returns the specific data set that correlates to a specific
     epoch
     Args:
     arg1 (int): epoch is the main parameter for the function and is an int to
     signify which epoch is being called in the command line (i.e. 2 = 2nd epoch)
     The app route can be called with '/epochs/(an integer)' and the route 
     retrieves the data set that is attatched to the specific epoch.
     Returns:
     The function returns the data set of the desired epoch (dictionary) 
     """
     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     for e in range(len(ds_statevector)):
         if(e == epoch):
             return ds_statevector[e]

@app.route('/epochs/<int:epoch>/speed', methods=['GET'])
def speedofepoch(epoch):
     """
     This function returns the speed of a desired epoch through obtaining the x dot,
     y dot, and z dot values and mathematically manipulating them through the speed 
     equation
     Args:
     arg1 (int): epoch is the main parameter for the function and is an int to
     signify which epoch is being called in the command line (i.e. 2 = 2nd epoch)
     The app route can be called with '/epochs/(an integer)/speed' and the route
     retrieves the speed of the data set.
     Returns:
     This function returns the speed of the epoch (string)
     """
     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     for e in range(len(ds_statevector)):
         if (e == epoch):
             xd = abs(float(ds_statevector[e]['X_DOT']['#text']))
             yd = abs(float(ds_statevector[e]['Y_DOT']['#text']))
             zd = abs(float(ds_statevector[e]['Z_DOT']['#text']))

             speed = round(math.sqrt(xd**2 + yd**2 + zd**2),3)
             return str(speed)
     return 0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')













from flask import Flask, request
import requests 
import xmltodict
import math

app = Flask(__name__)

url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
response = requests.get(url)

global data 
data = xmltodict.parse(response.text)

@app.route('/', methods=['GET'])
def dataset() -> dict:
    """
    This function returns all of the data from the XML file.
    Args:
    This function does not have a set parameter, but the app route can be called 
    with '/' and the route retrieves the data through 'GET'
    Returns:
    This function returns the data set as a dictionary
    """
    global data
    
    try:
        return data
    except:
        return "Error! Invalid repsonse :("
    
    return data

#@app.route('/epochs', methods=['GET'])
#def allepochs():
 #    """
  #   This function returns all of the epochs in the data set
   #  Args:
    # This function does not have a set parameter, but the app route can be called 
    # with '/epochs' and the route retrieves the data through 'GET'
    # Returns:
    # This function returns all the epochs (strings) in the ISS data set
    # """     
    # result = []
    # ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
    # for e in range(len(ds_statevector)):         
     #  result.append(ds_statevector[e]['EPOCH'])
    # return result

@app.route('/epochs', methods=['GET'])
def modifepoch() -> list:
     """
     This function returns a modified list of epochs given in the query parameters:
     limit and offest. When no limit or offset is given, the function will return 
     the entire data set.
     Args:
     This function does not have a set parameter, but the app route can be called
     with '/epochs' and the route retrieves the data through 'GET'. The route also 
     takes in a limit and offset that can be called with '/epochs?limit=int&offset
     =int'
     Returns:
     This function returns the epochs (strings) in the ISS data set as a list
     """
     global data
     result = []
     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     limit = request.args.get("limit", len(ds_statevector))
     try: 
         limit = int(limit)
     except: 
         return "Error! Invalid repsonse :("

     offset = request.args.get("offset", 0)
     try:
         offset = int(offset)
     except:
         return "Error! Invalid repsonse :("

     for l in range(limit):
         result.append(ds_statevector[offset+l]['EPOCH'])
     return result 

@app.route('/epochs/<int:epoch>', methods=['GET'])
def spefepochs(epoch:int) -> dict:
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
     global data

     try:
         epoch = int(epoch)
     except:
         return "Error! Invalid repsonse :("

     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     for e in range(len(ds_statevector)):
         if(e == epoch):
             return ds_statevector[e]

@app.route('/epochs/<int:epoch>/speed', methods=['GET'])
def speedofepoch(epoch:int) -> float: 
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
     global data

     try:
         epoch = int(epoch)
     except:
         return "Error! Invalid repsonse :("

     ds_statevector = data['ndm']['oem']['body']['segment']['data']['stateVector']
     for e in range(len(ds_statevector)):
         if (e == epoch):
             xd = abs(float(ds_statevector[e]['X_DOT']['#text']))
             yd = abs(float(ds_statevector[e]['Y_DOT']['#text']))
             zd = abs(float(ds_statevector[e]['Z_DOT']['#text']))

             speed = round(math.sqrt(xd**2 + yd**2 + zd**2),3)
             return str(speed)
     return 0

@app.route('/help', methods=['GET'])
def helpepoch() -> list:
    """
    This function returns strings that describe what each app route does and how to call
    each one.
    Args: This function does not have a set parameter, but the app route can be called
    with '/help' and the route retrieves the data through 'GET'.
    Returns:
    This function returns the app routes and their function as a list of strings 
    """
    helpstring = ["/: returns the whole data set",
            "/epochs?limit=int&offset=int: returns a modified list of Epochs with the parameters",
            "/epochs/<epoch: returns state vectors for a specific Epoch",
            "/epochs/<epoch>/speed: returns the speed for a specific Epoch",
            "/help: returns text that explains each app route",
            "/delete-data: deletes all the data from the  dictionary object",
            "/post-data: reloads the dictionary object with data from the web"]
            
    return helpstring

@app.route('/delete-data', methods=['DELETE'])
def deletedata() -> list :
    """
    This function deletes old state vectors from the global data variable.
    Args: This function does not have a set parameter, but the app route can be called
    with '/delete-data' and the route deletes the data through 'DELETE'.
    Returns:
    This function returns an empty data set (dictionary).
    """
    global data 
    data['ndm']['oem']['body']['segment']['data']['stateVector'] = []
    return []

@app.route('/post-data', methods=['POST'])
def postdata() -> dict:
    """
    This function returns an updated dictionary of data from the ISS XML data.
    Args: This function does not have a set parameter, but the app route can be called
    with '/post-data' and the route retrieves the data through 'POST'.
    Returns:
    This function returns the data set (dictionary).
    """
    global data
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')













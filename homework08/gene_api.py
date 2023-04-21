from flask import Flask, request, send_file
from collections import Counter, OrderedDict 
import os
import redis
import requests
import json
import matplotlib.py as plt
import numpy as np

app = Flask(__name__)

def get_redis_client1():
    redisIP1 = os.environ.get('REDIS_IP')
    if not redisIP1:
        raise Exception()
    redis1 = redis.Redis(host=redis_ip, port=6379, db=0, decode_responses=True)
    return redis1

def get_redis_client2():
    redisIP2 = os.environ.get('REDIS_IP')
    if not redisIP2:
        raise Exception()
    redis2 = redis.Redis(host=redis_ip1, port=6379, db=1)
    return redis2

def get_redis_client3():
    redisIP3 = os.environ.get('REDIS_IP')
    if not redisIP3:
        raise Exception()
    redis3 = redis.Redis(host=redis_ip2, port=6379, db=2, decode_responses=True)
    return redis3

rd1 = get_redis_client1()
rd2 = get_redis_client2()
rd3 = get_redis_client3()

def get_data():
    response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    response = response.json()['response']['docs']
    return response

@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def handle_data() -> dict:
    """
    This function can retrieve, store, and delete data from the Gene Names data base.
    Args:
    This function does not have a set parameter, but the approute can be called with
    '/data' to retrive and return the whole data set, '/data -X POST' to store the 
    data set, '/data -X DELETE' to remove the data.
    Returns:
    This function will return different outputs. For the GET method, it will return 
    a dictionary. For the POST method, it will return a message through a string 
    once the data set has been loaded. For the DELETE method, it will return a 
    message through a string.
    """
    if request.method == 'GET':
        output_list = []
        for item in rd1.keys():
            output_list.append(json.loads(rd1.get(item)))
        return output_list

    elif request.method == 'POST':
        data = get_data()
        for item in data:
            key = f'{item["hgnc_id"]}'
            rd1.set(key, json.dumps(item))
        return f'data loaded\n'
    
    elif request.method == 'DELETE':
        rd1.flushdb()
        return f'data deleted\n'
    else:
        return 'Method not applicable'

@app.route('/genes', methods=['GET'])
def gethgncID() -> list:
    """
    This function can retrieve and return a list of all the HGNC IDs.
    Args:
    This function does not have a set parameter, but the approute can be called with
    '/genes' and return a list of the IDs.
    Returns:
    This function will return a list.
    """
    try:
        rd1.keys()
    except KeyError:
        return ("No data available")

    hgnc_id_list = []
    data = get_data()
    for item in data:
        hgnc_id_list.append(item['hgnc_id'])
    return hgnc_id_list
    
@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def spefhgncID(hgnc_id:str) -> str:
    """
    This function can retrieve a string of information that relates to a specific 
    HGNC ID that the user inputs.
    Args:
    This function does set parameter, <hgnc_id:str>, a string! This is the specific
    HGNC ID that the user inputs. The app route can be called through
    'genes/(HGNC ID)' where the ID is inputted as a string.  
    Returns:
    This function will return a string.
    """
    try:
        rd1.keys()
    except KeyError:
        return("No data available")

    data = get_data()

    for g in range(len(data)):
        if(data[g]['hgnc_id'] == str(hgnc_id)):
            items = json.loads(rd.get(hgnc_id))
            return items

@app.route('/image', methods = ['POST','GET', 'DELETE'])
def get_image():
    """
    This route performs several tasks seamlessly, starting with retrieving data from the database, followed by generating a high-quality plot image, and finally storing the image back in the database. After that, the image is fetched from the database for further usage, and once its purpose is served, it is efficiently removed from the database.
    Args:
    This functionhas no set parameters but can be called through the route 
    '/image'
    Returns:
    (file_bytes): Returns the file_bytes of the image in the POST route.
    send_file(): Returns the image to the user in the GET route.
    """
    
    years = []
    counts = []
    if request.method == 'POST':
        for item in rd1.keys():
            gene = json.loads(rd1.get(item))
            year = gene['date_approved_reserved'][0:4]
            years.append(year)
        yeard = dict(Counter(years))
        years = list(yeard.keys())
        counts = list(yeard.values())
        plt.figure(figsize=(28,6))
        plt.bar(years, counts, width = 0.35)
        plt.xlabel("Years")
        plt.ylabel("Number of Entries Approved")
        plt.title("Genes Approved Each Year")
        plt.savefig('approvalyears.png')
        file_bytes = open('./approvalyears.png', 'rb').read()
        rd2.set('genes_approved', file_bytes)
        return ("Image created\n")
    
    elif request.method == 'GET':
        path = './myapprovalyears.png'
        with open(path, 'wb') as f:
            try:
                f.write(rd2.get('genes_approved'))
            except TypeError:
                return ("No image in the database\n")
            f.write(rd2.get('genes_approved'))
        return send_file(path, mimetype='image/png', as_attachment=True)

    elif request.method == 'DELETE':
        try:
            len(rd2.keys()) >= 1
        except Exception:
            return ("No image in the database to delete")
        rd2.flushdb()
        return f'Image deleted, there are {len(rd2.keys())} keys in the db\n'

    else:
        return 'The method you tried does not work\n'

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')

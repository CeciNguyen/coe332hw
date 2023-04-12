from flask import Flask, request
import redis
import requests
import json

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)

rd = get_redis_client()

@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def handle_data() -> dict:
    if request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list

    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        data = response.json
        for item in data()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            rd.set(item.get('hgnc_id'), json.dumps(item))
        return f'data loaded\n'
    
    elif request.method == 'DELETE':
        redis.flushdb()
        return f'data deleted\n'
    else:
        return 'Method not applicable'

@app.route('/genes', methods=['GET'])
def gethgncID() -> list:
    try:
        rd.keys()
    except KeyError:
        return ("No data available")

    hgnc_id_list = []
    response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    data = response.json
    for item in data()['response']['docs']:
        hgnc_id_list.append(item['hgnc_id'])
    return hgnc_id_list
    
@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def spefhgncID(hgnc_id:str) -> str:
    try:
        rd.keys()
    except KeyError:
        return("No data available")

    response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    data = response.json
    genedict = data()['response']['docs']

    for g in range(len(genedict)):
        if(genedict[g]['hgnc_id'] == str(hgnc_id)):
            items = json.loads(rd.get(hgnc_id))
            return items


if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')

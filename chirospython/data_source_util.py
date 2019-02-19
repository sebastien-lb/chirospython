import requests
import os
import sys

from flask import Response, json

# send status to the server
def send_status(value, data_source_name):
    data = {}
    # for now we only send the temp without the celsius
    data["value"] = value
    print("Sending Status")

    with open(os.path.join(sys.path[0], "server.json"), "r") as file:
        server = json.loads(file.read())
        try :
            data["data_source_id"] = server["data-source-ids"][data_source_name]
        except KeyError:
            print("ERROR data-source-ids unknown, try reconnecting the object to the server")
            return 

    requests.post("http://" + server["url"] + ":" + server["port"] + "/saveDataPoint", data=json.dumps(data),
                  headers={'Content-type': 'application/json'})
    
    print("Value Sent ", data["data_source_id"])    

    return Response(status=200)

# save state in state.json
def save_local_state(value, data_source_name):
    data = {}
    try:
        with open(os.path.join(sys.path[0], "state.json"), "r") as file:
            data = json.loads(file.read())
    except FileNotFoundError: 
        print("state.json does not exist, it is going to be created")

    data[data_source_name] = value

    with open(os.path.join(sys.path[0], "state.json"), "w") as file:
        file.write(json.dumps(data))

    
def get_saved_state(data_source_name):
    data = {}
    try:
        with open(os.path.join(sys.path[0], "state.json"), "r") as file:
            data = json.loads(file.read())
    except FileNotFoundError:
        print("WARNING: state.json does not exist")
        return None
    try:
        return data[data_source_name]
    except KeyError:
        print("WARNING:" + data_source_name + " has no saved state")
        return None
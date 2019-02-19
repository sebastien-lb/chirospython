
from flask import json, request, Response

import os
import sys

# Return json config to server
def getConfigResponse():
    data = {}
    with open(os.path.join(sys.path[0], "config.json")) as file:
        data = json.loads(file.read())
        print(data)
        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    
    response = Response(
        response=json.dumps(data),
        status=500,
        mimetype='application/json'
    )

    return response

# Save Server config return at object initialization
def setServerConfig():
    try:
        data = request.get_json(force=True)
        server_config = {}
        server_config["url"] = data.get("url")
        server_config["id"] = data.get("id")
        server_config["port"] = data.get("port")
        server_config["data-source-ids"] = data.get("data-source-ids")
    except:
        return Response(status=400)


    with open(os.path.join(sys.path[0], "server.json"), "w") as file:
        file.write(json.dumps(server_config))

    response = Response(
        status=200
    )
    return response



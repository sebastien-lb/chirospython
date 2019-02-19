
from flask import Flask, Response 

from .jsonConfig import getConfigResponse, setServerConfig
from .data_source_util import send_status, save_local_state, get_saved_state
from .system_handler import is_raspberry_pi

app = Flask(__name__)

def launch_app(port):
    app.run(port=port, host="0.0.0.0")

@app.route('/config')
def configRoute():
    return getConfigResponse()

@app.route('/serverConfig', methods=['POST'])
def serverConfigRoute():
    return setServerConfig()


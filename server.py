from logging import log
from time import sleep
from flask import Flask, render_template
from base import Configuration, logging

configuration = Configuration(confFile="configuration_dev.json")
server = Flask(__name__)
logger = logging.getLogger(server.name)

@server.route(configuration.viewEndpoint)
def index():
    logger.info("Request to GUI")
    return render_template('index.html')

@server.route(configuration.streamEndpoint)
def stream():
    logger.info("XMLHttpRequest for data stream")
    def generate():
        with open(configuration.logPath) as f:
            while True:
                yield f.read()
                sleep(1)

    return server.response_class(generate(), mimetype='text/plain')
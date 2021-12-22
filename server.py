from logging import log
from flask import Flask
from base import logging

server = Flask(__name__)
logger = logging.getLogger(server.name)

@server.route("/")
def run():
    logger.info("ProcessRequest to main route")
    return "<h2> LogViewer server is up </h2>"
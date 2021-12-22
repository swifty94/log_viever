from logging import log
from flask import Flask, render_template
from base import logging

server = Flask(__name__)
logger = logging.getLogger(server.name)

@server.route("/")
def run():
    logger.info("ProcessRequest to '/' route")
    text = "Some text"
    render_template('index.html', text=text) 
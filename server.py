from logging import log
from flask import Flask, render_template
from base import Configuration, LogContent, logging

configuration = Configuration(confFile="configuration_dev.json")
logViewer = LogContent(configuration.logPath)
server = Flask(__name__)
logger = logging.getLogger(server.name)

@server.route("/")
def run():
    text = logViewer.get_content()
    logger.info("ProcessRequest '/' route")
    logger.info(f"DataLengh: {len(text)}")
    return render_template('index.html', text=text)
from waitress import serve
from base import Configuration, LogViewerException, logging
from flask import Flask, render_template
from time import sleep

c = Configuration(confFile="configuration.json")
server = Flask(__name__)
logger = logging.getLogger(server.name)

@server.route(c.viewEndpoint)
def gui():
    logger.info("Request to GUI")
    return render_template('index.html')

@server.route('/stream')
def stream():
    logger.info("XMLHttpRequest for data stream")
    def generate():
        with open(c.logPath) as f:
            while True:
                yield f.read()
                sleep(1)

    return server.response_class(generate(), mimetype='text/plain')

if __name__ == "__main__":
    try:
        logging.info(f"---------- Application start ----------")        
        logging.info(f"Streming endpoint: http://{c.host}:{c.port}{c.streamEndpoint}")
        logging.info(f"GUI endpoint: http://{c.host}:{c.port}{c.viewEndpoint}")
        serve(server, host=c.host, port=c.port)
    except Exception as e:
        raise LogViewerException(f"Error occured in {__name__} module. Exception: {e}")
    finally:
        logging.info(f"---------- Application end ----------")
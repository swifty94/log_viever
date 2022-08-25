from ipaddress import ip_address
from base import logging
from server import server
from waitress import serve
from base import logging
from exceptions import LogViewerException
from base import Configuration

if __name__ == "__main__":
    c = Configuration()
    try:
        logging.info(f"---------- Application start ----------")        
        logging.info(f"Streming endpoint: http://{c.host}:{c.port}{c.streamEndpoint}")
        logging.info(f"GUI endpoint: http://{c.host}:{c.port}{c.viewEndpoint}")
        serve(server, host=c.host, port=c.port)
    except Exception as e:
        raise LogViewerException(f"Error occured in {__name__} module. Exception: {e}")
    finally:
        logging.info(f"---------- Application end ----------")
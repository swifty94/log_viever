import logging, json
import logging.config
from os import path
from shutil import copyfile
logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))

class LogViewerException(Exception):
    """Base applicaton Exception"""
    def __init__(self, message="Error occured"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        logging.error(f"{self.message}", exc_info=1)
        return f'-> {self.message}'
class Configuration(object):
    """
    JSON configuration object\n
    Available properties:
        - logPath - path to log\n
        - host - IP addr to listen\n
        - port - tcp port to listen\n
        - streamEndpoint - e.g., '/stream'\n
        - viewEndpoint - e.g., '/log'\n
    """
    def __init__(self, confFile="configuration.json") -> object:
        super().__init__()
        self.confFile = confFile
        self.logPath = self._get("logPath")
        self.host = self._get("host")
        self.port = self._get("port")
        self.streamEndpoint = self._get("streamEndpoint")
        self.viewEndpoint = self._get("viewEndpoint")
        copyfile(confFile, "static/")
    
    def _get(self, key) -> str:
        """
        Get JSON value by key
        :param - key:str
        :param - return:str
        """
        try:
            with open(self.confFile) as f:
                data = json.load(f)
            val = data[key]    
            return val
        except FileNotFoundError as noF:
            _l = f"CriticalException {noF} -> AppExit!"
            raise LogViewerException(_l)
        except Exception as e:
            raise LogViewerException(e)
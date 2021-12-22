import logging, json
import logging.config
from os import path
logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))
from exceptions import LogViewerException

class Configuration(object):
    """
    JSON configuration object\n
    Available properties:
        - logPath - path to log
    """
    def __init__(self, confFile="configuration.json") -> object:
        super().__init__()
        self.confFile = confFile
        self.logPath = self._get("logPath")
    
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

class LogContent(object):
    """ 
    Log content class 
    method - get_content() -> return log as str
    """
    def __init__(self, pathToLog: str) -> None:
        """
        param pathToLog: str - full path to the log file you wish to track
        """
        super().__init__()
        self.pathToLog = pathToLog

    def get_content(self) -> str:
        """
        param - None
        return - self.pathToLog content as String
        """
        try:
            with open(self.pathToLog, "r") as f:
                return f.read()
        except Exception as e:
            raise LogViewerException(e)

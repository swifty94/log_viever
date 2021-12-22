import logging, json
import logging.config
from os import path
logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))
from exceptions import LogViewerException

class Configuration(object):
    """
    JSON configuration object\n
    Available properties:
    - API_KEY - Telegram bot API key
    - DAYS_SECONDS - Amount of time bot will be alive
    - TIMEOUT - Timeout between each reminder from bot
    """
    def __init__(self, confFile="configuration.json") -> object:
        super().__init__()
        self.logger = logging.getLogger(__class__.__name__)
        self.confFile = confFile
        self.logPath = self._get("logPath")
        self.user = self._get("user")
        self.password = self._get("password")
    
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
            self.logger.info(f"ProcessedKey: {key}")       
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
        self.logger = logging.getLogger(__class__.__name__)
        self.pathToLog = pathToLog
        self.logger.info(f'LogForProcessing: {self.pathToLog}')

    def get_content(self):
        try:
            self.logger.info(f'ProcessingFileContent: {self.pathToLog}')
            with open(self.pathToLog, "r") as f:
                return f.read()
        except Exception as e:
            raise LogViewerException(e)

import logging
import logging.config
from os import path
logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))
from base import logging

class LogViewerException(Exception):
    """Base applicaton Exception"""
    def __init__(self, message="Error occured"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        logging.error(f"{self.message}", exc_info=1)
        return f'-> {self.message}'
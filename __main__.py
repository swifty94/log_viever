if __name__ == "__main__":
    try:
        logging.info(f"---------- Application start ----------")
        from server import server
        from waitress import serve
        from base import logging
        from exceptions import LogViewerException
        serve(server)
    except Exception as e:
        raise LogViewerException(f"Error occured in {__name__} module. Exception: {e}")
    finally:
        logging.info(f"---------- Application end ----------")
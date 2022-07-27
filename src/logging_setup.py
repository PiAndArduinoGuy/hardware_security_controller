import logging

class LoggingSetup():
    def __init__(self, logging_file_directory: str):
        try:
            LOGGER.info(f"Creating logging directory {logging_file_directory}")
            os.makedirs(os.getcwd() + f"/{logging_file_directory}")
        except FileExistsError:
            LOGGER.info(f"Logging directory {logging_file_directory} already exists.")
        logging.basicConfig(filename=os.getcwd() + logging_file_directory + '/hardware-security-controller.log',
                            level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(module)s:%(funcName)s(%(threadName)s)[%(lineno)d]:%(message)s')
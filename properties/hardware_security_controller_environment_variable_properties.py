from hardware_security_controller_properties import HardwareSecurityControllerProperties
from os import environ


class HardwareSecurityControllerEnvironmentVariableProperties(HardwareSecurityControllerProperties):
    def __init__(self):
        super().__init__()

    def set_security_micro_service_host_ip(self):
        self._security_micro_service_host_ip = environ['SECURITY_MICRO_SERVICE_HOST_IP']

    def set_security_micro_service_host_port(self):
        self._security_micro_service_host_port = environ['SECURITY_MICRO_SERVICE_HOST_PORT']

    def set_password(self):
        self._password = environ['PASSWORD']

    def set_logging_file_directory(self):
        self._logging_file_directory = environ['LOGGING_FILE_DIRECTORY']

import argparse

from properties.hardware_security_controller_properties import HardwareSecurityControllerProperties


class HardwareSecurityControllerCommandLineProperties(HardwareSecurityControllerProperties):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument("--logging_file_directory", required=True)
        parser.add_argument("--security_micro_service_host_ip", required=True)
        parser.add_argument("--security_micro_service_host_port", required=True)
        parser.add_argument("--password", required=True)
        self.arguments = vars(parser.parse_args())
        self.set_hardware_security_controller_properties()

    def set_security_micro_service_host_ip(self):
        self._security_micro_service_host_ip = self.arguments["security_micro_service_host_ip"]

    def set_security_micro_service_host_port(self):
        self._security_micro_service_host_port = self.arguments["security_micro_service_host_port"]

    def set_password(self):
        self._password = self.arguments["password"]

    def set_logging_file_directory(self):
        self._logging_file_directory = self.arguments["logging_file_directory"]

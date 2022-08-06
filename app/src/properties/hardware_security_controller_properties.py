from abc import ABC, abstractmethod

from properties.validation.harware_security_controller_properties_validator import \
    HardwareSecurityControllerPropertiesValidator


class HardwareSecurityControllerProperties(ABC):
    def __init__(self):
        self._security_micro_service_host_ip = None
        self._security_micro_service_host_port = None
        self._password = None
        self._logging_file_directory = None

    @abstractmethod
    def set_security_micro_service_host_ip(self):
        pass

    @abstractmethod
    def set_security_micro_service_host_port(self):
        pass

    @abstractmethod
    def set_password(self):
        pass

    @abstractmethod
    def set_logging_file_directory(self):
        pass

    def get_security_micro_service_host_ip(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._security_micro_service_host_ip)
        return self._security_micro_service_host_ip

    def get_security_micro_service_host_port(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._security_micro_service_host_port)
        return self._security_micro_service_host_port

    def get_password(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._password)
        return self._password

    def get_logging_file_directory(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._logging_file_directory)
        return self._logging_file_directory

    def set_hardware_security_controller_properties(self):
        self.set_security_micro_service_host_port()
        self.set_security_micro_service_host_ip()
        self.set_password()
        self.set_logging_file_directory()

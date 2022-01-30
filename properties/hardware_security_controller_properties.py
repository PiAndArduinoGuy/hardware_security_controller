from abc import ABC, abstractmethod

from properties.validation.harware_security_controller_properties_validator import \
    HardwareSecurityControllerPropertiesValidator


class HardwareSecurityControllerProperties(ABC):
    def __init__(self):
        self._security_micro_service_host = None
        self._security_micro_service_port = None
        self._password = None
        self._logging_file_location = None

    @abstractmethod
    def set_security_micro_service_host(self):
        pass

    @abstractmethod
    def set_security_micro_service_port(self):
        pass

    @abstractmethod
    def set_password(self):
        pass

    @abstractmethod
    def set_logging_file_location(self):
        pass

    def get_security_micro_service_host(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._security_micro_service_host)
        return self._security_micro_service_host

    def get_security_micro_service_port(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._security_micro_service_port)
        return self._security_micro_service_port

    def get_password(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._password)
        return self._password

    def get_logging_file_location(self):
        HardwareSecurityControllerPropertiesValidator.validate_property_non_null(self._logging_file_location)
        return self._logging_file_location

    def set_hardware_security_controller_properties(self):
        self.set_security_micro_service_port()
        self.set_security_micro_service_host()
        self.set_password()
        self.set_logging_file_location()

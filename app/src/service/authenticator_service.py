from properties.hardware_security_controller_properties import HardwareSecurityControllerProperties


class AuthenticatorService:
    def __init__(self,
                 hardware_security_controller_properties: HardwareSecurityControllerProperties):
        self.password = hardware_security_controller_properties.get_password()

    def authenticate(self, entered_password):
        return entered_password == self.password

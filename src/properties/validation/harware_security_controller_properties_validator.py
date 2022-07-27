from src.properties.validation.hardware_security_controller_properties_error import \
    HardwareSecurityControllerPropertiesError


class HardwareSecurityControllerPropertiesValidator:
    @staticmethod
    def validate_property_non_null(hardware_security_controller_property):
        if hardware_security_controller_property is None:
            raise HardwareSecurityControllerPropertiesError(
                "A hardware security controller property has a none value, the set_hardware_security_controller_properties method needs to "
                "be called prior to accessing any properties.")

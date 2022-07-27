from observer.keypad_observer import KeypadObserver
from observer.message_observer import MessageObserver
from properties.hardware_security_controller_environment_variable_properties import \
    HardwareSecurityControllerEnvironmentVariableProperties
from properties.hardware_security_controller_properties import HardwareSecurityControllerProperties
from security_micro_service_client import SecurityMicroServiceClient
from service.authenticator_service import AuthenticatorService
from service.hardware_alarm_interactor_service import HardwareAlarmInteractorService
from subject.keypad_subject import KeypadSubject
from subject.message_subject import MessageSubject
from logging_setup import LoggingSetup

if __name__ == '__main__':
    hardware_security_controller_properties: HardwareSecurityControllerProperties = \
        HardwareSecurityControllerEnvironmentVariableProperties()
    logging_setup = LoggingSetup(hardware_security_controller_properties.get_logging_file_directory())
    keypad = KeypadSubject()
    message_subject = MessageSubject()
    security_micro_service_client = SecurityMicroServiceClient(hardware_security_controller_properties,
                                                               message_subject)
    authenticator_service = AuthenticatorService(hardware_security_controller_properties)

    hardware_alarm_interactor_service = HardwareAlarmInteractorService(authenticator_service,
                                                                       security_micro_service_client)

    message_observer = MessageObserver(message_subject, "*/D/A/other,arm/disarm/acpt/pswd")
    keypad_observer = KeypadObserver(subject=keypad,
                                     hardware_alarm_interactor_service=hardware_alarm_interactor_service)

    keypad._get_pressed_keys()

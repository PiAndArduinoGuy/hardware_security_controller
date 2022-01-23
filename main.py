import sys

from observer.keypad_observer import KeypadObserver
from observer.message_observer import MessageObserver
from subject.keypad_subject import KeypadSubject
from security_micro_service_client import SecurityMicroServiceClient
from service.authenticator_service import AuthenticatorService
from service.hardware_alarm_interactor_service import HardwareAlarmInteractorService
from subject.message_subject import MessageSubject

if __name__ == '__main__':
    command_line_arguments = sys.argv[1:]
    password = command_line_arguments[0]
    security_micro_service_host = command_line_arguments[1]
    security_micro_service_port = command_line_arguments[2]

    keypad = KeypadSubject()
    message_subject = MessageSubject()
    security_micro_service_client = SecurityMicroServiceClient(security_micro_service_host,
                                                               security_micro_service_port,
                                                               message_subject)
    authenticator_service = AuthenticatorService(password)

    hardware_alarm_interactor_service = HardwareAlarmInteractorService(authenticator_service,
                                                                       security_micro_service_client)

    message_observer = MessageObserver(message_subject, "*/D/A/other,arm/disarm/acpt/pswd")
    keypad_observer = KeypadObserver(subject=keypad,
                                     hardware_alarm_interactor_service=hardware_alarm_interactor_service)

    keypad._get_pressed_keys()

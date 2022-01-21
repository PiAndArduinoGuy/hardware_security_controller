import sys

from observer.keypad_observer import KeypadObserver
from subject.keypad_subject import KeypadSubject
from security_micro_service_client import SecurityMicroServiceClient
from service.authenticator_service import AuthenticatorService
from service.hardware_alarm_interactor_service import HardwareAlarmInteractorService

if __name__ == '__main__':
    command_line_arguments = sys.argv[1:]
    password = command_line_arguments[0]
    security_micro_service_host = command_line_arguments[1]
    security_micro_service_port = command_line_arguments[2]

    keypad = KeypadSubject()
    security_micro_service_client = SecurityMicroServiceClient(security_micro_service_host,
                                                               security_micro_service_port)
    authenticator_service = AuthenticatorService(password)

    hardware_alarm_interactor_service = HardwareAlarmInteractorService(authenticator_service,
                                                                       security_micro_service_client)

    keypad_observer = KeypadObserver(subject=keypad,
                                     hardware_alarm_interactor_service=hardware_alarm_interactor_service)

    keypad._get_pressed_keys()

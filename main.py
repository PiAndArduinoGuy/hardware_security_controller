import sys

from service.authenticator_service import AuthenticatorService
from service.hardware_alarm_interactor_service import HardwareAlarmInteractor
from service.keypad_service import Keypad
from security_micro_service_client import SecurityMicroServiceClient

if __name__ == '__main__':
    command_line_arguments = sys.argv[1:]
    password = command_line_arguments[0]
    security_micro_service_host = command_line_arguments[1]
    security_micro_service_port = command_line_arguments[2]

    keypad = Keypad()
    security_micro_service_client = SecurityMicroServiceClient(security_micro_service_host,
                                                               security_micro_service_port)
    authenticator_service = AuthenticatorService(password)
    hardware_alarm_interactor = HardwareAlarmInteractor(subject=keypad,
                                                        keypad_commands=['*', 'D'],
                                                        authenticator_service=authenticator_service,
                                                        security_micro_service_client=security_micro_service_client)

    keypad._get_pressed_keys()

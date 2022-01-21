import sys

from authenticator_service import AuthenticatorService
from keypad import Keypad
from security_micro_service_client import SecurityMicroServiceClient

if __name__ == '__main__':
    command_line_arguments = sys.argv[1:]
    password = command_line_arguments[0]
    security_micro_service_host = command_line_arguments[1]
    security_micro_service_port = command_line_arguments[2]

    keypad = Keypad()
    security_micro_service_client = SecurityMicroServiceClient(security_micro_service_host,
                                                               security_micro_service_port)
    concrete_observer = AuthenticatorService(subject=keypad,
                                             keypad_commands=['*', 'D'],
                                             password=password,
                                             security_micro_service_client=security_micro_service_client)

    keypad._get_pressed_keys()

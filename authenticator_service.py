from requests import Response

from observer_design_pattern.observer import Observer
from observer_design_pattern.subject import Subject
import requests

from security_micro_service_client import SecurityMicroServiceClient


class AuthenticatorService(Observer):
    def __init__(self,
                 subject: Subject,
                 password: str,
                 keypad_commands: list,
                 security_micro_service_client: SecurityMicroServiceClient):
        super().__init__(subject)
        self.subject.add_observer(self)
        self.password = password
        self.keypad_commands = keypad_commands
        self.security_micro_service_client = security_micro_service_client

    def update(self):
        pressed_keys = self.subject.get_state()
        print(f"Received pressed keys - {pressed_keys}")
        if pressed_keys not in self.keypad_commands:
            print("Password detected.")
            if pressed_keys == self.password:
                print("Password correct. Requesting that the alarm be silenced.")
                self.security_micro_service_client.silence_alarm()

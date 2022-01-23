import requests

from subject.message_subject import MessageSubject


class SecurityMicroServiceClient:
    def __init__(self,
                 security_micro_service_host,
                 security_micro_service_port,
                 message_subject: MessageSubject):
        self.base_security_micro_service_url = 'http://' + security_micro_service_host + ":" + security_micro_service_port + \
                                               '/security'
        self.message_subject = message_subject

    def silence_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/silence-alarm')
        self.handle_response_with_messages(response, "Alarm silenced.", "Failed to silence.")

    def arm_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/arm-alarm')
        self.handle_response_with_messages(response, "Alarm armed.", "Failed to arm.")

    def disarm_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/disarm-alarm')
        self.handle_response_with_messages(response, "Alarm disarmed.", "Failed to disarm.")


    def handle_response_with_messages(self,response, success_message: str, failure_message: str):
        if response.ok:
            print(success_message)
            self.message_subject.set_message(success_message)
        else:
            print(f"{failure_message} Response code was {response.status_code} "
                  f"with response body {response.json()}")
            self.message_subject.set_message(failure_message)

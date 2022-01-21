import requests


class SecurityMicroServiceClient:
    def __init__(self,
                 security_micro_service_host,
                 security_micro_service_port):
        self.base_security_micro_service_url = 'http://' + security_micro_service_host + ":" + security_micro_service_port + \
                                               '/security'

    def silence_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/silence-alarm')
        self.handle_response_with_messages(response, "Alarm successfully silenced.", "ailed to silence alarm.")

    def arm_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/arm-alarm')
        self.handle_response_with_messages(response, "Alarm successfully armed.", "Failed to arm alarm.")

    def disarm_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/disarm-alarm')
        self.handle_response_with_messages(response, "Alarm successfully disarmed.", "Failed to disarm alarm.")

    @staticmethod
    def handle_response_with_messages(response, success_message: str, failure_message: str):
        if response.ok:
            print(success_message)
        else:
            print(f"{failure_message} Response code was {response.status_code} "
                  f"with response body {response.json()}")

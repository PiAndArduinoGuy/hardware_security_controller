import requests


class SecurityMicroServiceClient:
    def __init__(self,
                 security_micro_service_host,
                 security_micro_service_port):
        self.base_security_micro_service_url = 'http://' + security_micro_service_host + ":" + security_micro_service_port + \
                                               '/security'

    def silence_alarm(self):
        response = requests.put(self.base_security_micro_service_url + '/silence-alarm')
        if response.ok:
            print("Alarm successfully silenced.")
        else:
            print(f"Failed to silence alarm. Response code was {response.status_code} "
                  f"with response body {response.json()}")

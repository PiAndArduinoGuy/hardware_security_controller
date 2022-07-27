import logging

import requests

from properties.hardware_security_controller_properties import HardwareSecurityControllerProperties
from subject.message_subject import MessageSubject

LOGGER = logging.getLogger(__name__)


class SecurityMicroServiceClient:
    def __init__(self,
                 hardware_security_controller_properties: HardwareSecurityControllerProperties,
                 message_subject: MessageSubject):
        self.base_security_micro_service_url = 'http://' + \
                                               hardware_security_controller_properties.get_security_micro_service_host_ip() \
                                               + ":" + hardware_security_controller_properties.get_security_micro_service_host_port() + \
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

    def handle_response_with_messages(self, response, success_message: str, failure_message: str):
        if response.ok:
            LOGGER.info(success_message)
            self.message_subject.set_message(success_message)
        else:
            LOGGER.info("%s Response code was %s with response body %s", failure_message, response.status_code,
                        response.json())
            self.message_subject.set_message(failure_message)

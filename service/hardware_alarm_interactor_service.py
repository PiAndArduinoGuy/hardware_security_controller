from security_micro_service_client import SecurityMicroServiceClient
from service.authenticator_service import AuthenticatorService


class HardwareAlarmInteractorService:
    def __init__(self,
                 authenticator_service: AuthenticatorService,
                 security_micro_service_client: SecurityMicroServiceClient):
        self.commands = ['*', 'D']
        self.authenticator_service = authenticator_service
        self.security_micro_service_client = security_micro_service_client

    def handle_request(self, request):
        if request not in self.commands:
            print("Password detected.")
            if self.authenticator_service.authenticate(request):
                print("Password correct. Requesting that the alarm be silenced.")
                self.security_micro_service_client.silence_alarm()
        elif request == '*':
            print("Arm request received.")
            self.security_micro_service_client.arm_alarm()
        elif request == 'D':
            print("Disarm request received.")
            self.security_micro_service_client.disarm_alarm()

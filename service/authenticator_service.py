class AuthenticatorService:
    def __init__(self,
                 password: str):
        self.password = password

    def authenticate(self, entered_password):
        return entered_password == self.password

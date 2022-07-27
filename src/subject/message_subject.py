from src.observer_design_pattern.subject import Subject


class MessageSubject(Subject):
    def __int__(self):
        super().__init__()

    def set_message(self, message):
        self.set_state(message)


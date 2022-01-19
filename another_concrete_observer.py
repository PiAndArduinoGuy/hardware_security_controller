from observer_design_pattern.observer import Observer
from observer_design_pattern.subject import Subject


class AnotherConcreteObserver(Observer):
    def __init__(self, subject: Subject):
        super().__init__(subject)
        self.subject.add_observer(self)

    def update(self):
        print(f"Received an update (AnotherConcreteObserver) {self.subject.get_state()}")

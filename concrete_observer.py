from observer_design_pattern.observer import Observer
from observer_design_pattern.subject import Subject


class ConcreteObserver(Observer):
    def __init__(self, subject: Subject):
        super().__init__(subject)
        self.subject.add_observer(self)

    def update(self):
        print(f"Received an update (ConcreteObserver) {self.subject.get_state()}")
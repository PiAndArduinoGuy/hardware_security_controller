from src.observer_design_pattern.observer import Observer
from src.observer_design_pattern.subject import Subject

from src.service.hardware_alarm_interactor_service import HardwareAlarmInteractorService
import logging
LOGGER = logging.getLogger(__name__)

class KeypadObserver(Observer):
    def __init__(self,
                 subject: Subject,
                 hardware_alarm_interactor_service: HardwareAlarmInteractorService):
        super().__init__(subject)
        self.subject.add_observer(self)
        self.hardware_alarm_interactor_service = hardware_alarm_interactor_service

    def update(self):
        pressed_keys = self.subject.get_state()
        LOGGER.info(f"Received pressed keys - %s", pressed_keys)
        self.hardware_alarm_interactor_service.handle_request(pressed_keys)

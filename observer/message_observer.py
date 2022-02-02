import time

from rpi_lcd import LCD

from observer_design_pattern.observer import Observer
import logging

LOGGER = logging.getLogger(__name__)


class MessageObserver(Observer):
    def __init__(self, subject, default_message):
        super().__init__(subject)
        self.lcd = LCD()
        self.subject.add_observer(self)
        self.default_message = default_message
        self.display_default_message()

    def update(self):
        self.display_text(self.subject.get_state())
        time.sleep(5)
        self.display_default_message()

    def display_default_message(self):
        self.lcd.clear()
        self.display_text(self.default_message)

    def display_text(self, text):
        self.lcd.clear()
        first_row_text = text[0:16]
        second_row_text = text[16:32]
        self.lcd.text(first_row_text, 1)
        self.lcd.text(second_row_text, 2)
        if text[32:] is not '':
            LOGGER.error(f"Could not fit '%s' onto display.", text[32:])

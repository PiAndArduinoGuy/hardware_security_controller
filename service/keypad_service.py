import time

import adafruit_matrixkeypad
import board
import digitalio

from observer_design_pattern.subject import Subject


class Keypad(Subject):
    def __init__(self):
        super(Keypad, self).__init__()
        rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
        cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D20, board.D11, board.D9)]
        keys = ((1, 2, 3, "A"),
                (4, 5, 6, "B"),
                (7, 8, 9, "C"),
                ("*", 0, "#", "D"))

        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    def get_latest_entered_keys_string(self):
        return self.get_state()

    @staticmethod
    def create_string_from_keys_array(entered_keys_array):
        entered_keys_string = ''
        for key in entered_keys_array:
            entered_keys_string += str(key)
        return entered_keys_string

    def _get_pressed_keys(self):
        def _is_accept_key(pressed_key):
            return pressed_key == 'A'

        def _keys_not_yet_pressed(pressed_keys):
            return len(pressed_keys) == 0

        entered_keys_array = []
        print('Listening for keypad presses...')
        while True:
            if not _keys_not_yet_pressed(self.keypad.pressed_keys):
                pressed_key = self.keypad.pressed_keys[0]
                if _is_accept_key(pressed_key):
                    self.set_state(self.create_string_from_keys_array(entered_keys_array))
                    entered_keys_array = []
                else:
                    entered_keys_array.append(pressed_key)
            time.sleep(0.2)

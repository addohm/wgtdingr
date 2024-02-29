import threading
import pyautogui
import keyboard
import pydirectinput
from win32gui import GetForegroundWindow, GetWindowText, GetWindowRect
# ^^^ ^^^ ^^^ ^^^ pip install pywin32

WINDOW_NAME = "WGT Golf"
VERBOSE = True
DEBUG = True
global run_flag
run_flag = False

def toggle_run():
    global run_flag
    run_flag = not run_flag

class ReportMouseColor(threading.Thread):
    mcol = 0
    def run(self):
        while True:
            self.mpos = pyautogui.position()
            self.mcol = pyautogui.pixel(
                (pyautogui.position().x),
                (pyautogui.position().y)
            )


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl', toggle_run)
    mrcthread = ReportMouseColor()
    mrcthread.start()
    active = False
    while True:
        if not run_flag:
            # Script inactive
            if active: print('Deactivated.')
            active = False
        if run_flag:
            # Script active
            if not active: print('Active...')
            active = True
            window = GetForegroundWindow()
            if GetWindowText(window) == WINDOW_NAME:
                if mrcthread.mcol == (156,242,80):
                    pydirectinput.click()
                    toggle_run()

import threading
import pyautogui
import pydirectinput
import tkinter as tk
from PIL import Image, ImageTk
from win32gui import GetForegroundWindow, GetWindowText, GetWindowRect
# ^^^ ^^^ ^^^ ^^^ pip install pywin32

WINDOW_NAME = "WGT Golf"
VERBOSE = True
DEBUG = True

# Thread class to report mouse color
class ReportMouseColor(threading.Thread):
    mcol = (0, 0, 0)  # Initialize with black color
    def run(self):
        while True:
            window = GetForegroundWindow()
            if GetWindowText(window) == WINDOW_NAME:
                self.mpos = pyautogui.position()
                self.mcol = pyautogui.pixel(self.mpos.x, self.mpos.y)

class ClickMouseColor(threading.Thread):
     def run(self):
          while True:
            window = GetForegroundWindow()
            if GetWindowText(window) == WINDOW_NAME:
                    if rmcthread.mcol == (156,242,80):
                        pydirectinput.click()

if __name__ == '__main__':
    rmcthread = ReportMouseColor()
    rmcthread.start()
    cmcthread = ClickMouseColor()
    cmcthread.start()
    # # Create a tkinter window
    # root = tk.Tk()
    # root.title("Power Meter")

    # # Load the image
    # image = Image.open("assets/generated_marks.png")

    # # Resize the image if needed
    # # image = image.resize((width, height), Image.ANTIALIAS)

    # # Convert the image to a format that tkinter can display
    # photo = ImageTk.PhotoImage(image)

    # # Create a label widget to display the image
    # label = tk.Label(root, image=photo)
    # label.pack()

    # # Run the tkinter event loop
    # root.mainloop()

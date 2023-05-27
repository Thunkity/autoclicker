import keyboard
import pyautogui
import os
import tkinter as tk
from threading import Thread

is_autoclicking = False
start_stop_key = "["

def toggle_autoclick():
    global is_autoclicking
    if is_autoclicking:
        is_autoclicking = False
        status_label.config(text="Autoclicker stopped.")
    else:
        is_autoclicking = True
        status_label.config(text="Autoclicker started.")

def stop_script():
    status_label.config(text="Autoclicker closed.")
    os._exit(0)

def autoclicker(interval):
    while True:
        if is_autoclicking:
            pyautogui.click()
        pyautogui.PAUSE = interval

def start_autoclicker():
    interval = float(interval_entry.get())
    autoclick_thread = Thread(target=autoclicker, args=(interval,))
    autoclick_thread.daemon = True
    autoclick_thread.start()

# create window
window = tk.Tk()
window.title("Autoclicker")
window.geometry("450x200")

# set window non-resizable
window.resizable(False, False)

# create interval input field
interval_label = tk.Label(window, text="Enter the interval between clicks (in seconds):")
interval_label.grid(row=0, column=0)

interval_entry = tk.Entry(window)
interval_entry.grid(row=0, column=1)

# create start button
start_button = tk.Button(window, text="Set Interval", command=start_autoclicker)
start_button.grid(row=0, column=2)

# create status label
status_label = tk.Label(window, text="Push [ to start and stop the autoclicker.")
status_label.grid(row=1, columnspan=3)

# hotkeys
keyboard.add_hotkey(start_stop_key, toggle_autoclick)

window.mainloop()

import tkinter as tk
import keyboard
import pyperclip
import threading
import time
import re

# Initialize root window (hidden)
root = tk.Tk()
root.withdraw()

# Overlay window setup
overlay = tk.Toplevel(root)
overlay.title("Players Overlay")
overlay.geometry("300x150")
overlay.configure(bg="black")
overlay.attributes("-topmost", True)
overlay.overrideredirect(True)

# Window close handling
window_closed = False

def on_closing():
    global window_closed
    window_closed = True
    root.quit()
    overlay.destroy()

overlay.protocol("WM_DELETE_WINDOW", on_closing)

# Close button (only visible on hover)
close_button = tk.Button(
    overlay,
    text="X",
    command=on_closing,
    bg="red",
    fg="white",
    bd=0,
    font=("Helvetica", 12, "bold")
)
close_button.place(x=270, y=5)
close_button.place_forget()

def show_close(event=None):
    close_button.place(x=270, y=5)

def hide_close(event=None):
    close_button.place_forget()

overlay.bind("<Enter>", show_close)
overlay.bind("<Leave>", hide_close)

# Labels
label_header = tk.Label(
    overlay,
    text="PLAYERS",
    fg="yellow",
    bg="black",
    font=("Helvetica", 24, "bold")
)
label_header.pack(padx=20, pady=10)

label_value = tk.Label(
    overlay,
    text="None",
    fg="lightgreen",
    bg="black",
    font=("Helvetica", 32, "bold")
)
label_value.pack(padx=20, pady=0)

# Input tracking variables
typed_buffer = ""
clipboard_buffer = None
ctrl_v_pressed = False

# Update label value
def update_value(text):
    match = re.search(r"/players\s*([1-8])", text)
    if match:
        value = match.group(1)
        label_value.config(text=value, fg="lightblue")

# Keyboard listener logic
def keyboard_listener():
    global typed_buffer, clipboard_buffer, ctrl_v_pressed

    def on_key(e):
        global typed_buffer, clipboard_buffer, ctrl_v_pressed

        if e.name == "enter":
            if ctrl_v_pressed and clipboard_buffer:
                if "/players" in clipboard_buffer:
                    if typed_buffer and typed_buffer in [str(x) for x in range(1, 9)]:
                        clipboard_buffer = clipboard_buffer.split()[0] + ' ' + typed_buffer
                    update_value(clipboard_buffer)
                clipboard_buffer = None
                ctrl_v_pressed = False
            elif "/players" in typed_buffer:
                update_value(typed_buffer)
            typed_buffer = ""
        elif keyboard.is_pressed("ctrl") and e.name == "v":
            try:
                clipboard_buffer = pyperclip.paste()
                ctrl_v_pressed = True
            except Exception:
                pass
        elif e.name in {"ctrl", "shift", "alt", "tab"}:
            return
        elif e.name == "space":
            typed_buffer += " "
        elif e.name == "backspace":
            typed_buffer = typed_buffer[:-1]
        elif len(e.name) == 1:
            typed_buffer += e.name
        elif e.name.startswith("num") and len(e.name) == 4 and e.name[-1].isdigit():
            typed_buffer += e.name[-1]

        if len(typed_buffer) > 30:
            typed_buffer = ""

    keyboard.on_press(on_key)

    while not window_closed:
        time.sleep(0.05)

# Start listener thread
def start_threads():
    threading.Thread(target=keyboard_listener, daemon=True).start()

# Run application
start_threads()
root.mainloop()

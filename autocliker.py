import threading
import time
import tkinter as tk

try:
    import keyboard
except ImportError:
    raise ImportError("Please install the 'keyboard' library by running: pip install keyboard")

# Simple Auto Key Presser GUI
# Presses the 'E' key repeatedly at a customizable interval when started.
class AutoKeyPresser:
    def __init__(self, master):
        self.master = master
        master.title("Auto Key Presser")
        master.resizable(False, False)
        master.geometry("300x250")  # Set initial window size (width x height)

        # Default interval (seconds) and control variable
        self.interval = 0.1
        self.interval_var = tk.DoubleVar(value=self.interval)

        # Interval setting
        interval_frame = tk.Frame(master)
        interval_frame.pack(pady=5)
        tk.Label(interval_frame, text="Interval (s):").pack(side=tk.LEFT)
        self.interval_spinbox = tk.Spinbox(
            interval_frame,
            from_=0.01,
            to=10.0,
            increment=0.01,
            textvariable=self.interval_var,
            width=5
        )
        self.interval_spinbox.pack(side=tk.LEFT)

        # Status Label
        self.status_label = tk.Label(master, text="Status: Stopped")
        self.status_label.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(master, text="Start", width=10, command=self.start)
        self.start_button.pack(pady=5)

        # Stop Button
        self.stop_button = tk.Button(master, text="Stop", width=10, state=tk.DISABLED, command=self.stop)
        self.stop_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(master, text="Exit", width=10, command=master.quit)
        self.exit_button.pack(pady=5)

        # Thread handle
        self.running = False
        self.thread = None

    def press_key_loop(self):
        while self.running:
            keyboard.send('e')
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            # Update interval from GUI
            try:
                self.interval = float(self.interval_var.get())
            except Exception:
                self.interval = 0.1

            self.running = True
            self.thread = threading.Thread(target=self.press_key_loop, daemon=True)
            self.thread.start()
            self.status_label.config(text="Status: Running")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        if self.running:
            self.running = False
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=0.1)
            self.status_label.config(text="Status: Stopped")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoKeyPresser(root)

    # Register global hotkey Ctrl+Shift+E to toggle start/stop
    keyboard.add_hotkey(
        'ctrl+shift+e',
        lambda: root.after(0, app.start) if not app.running else root.after(0, app.stop)
    )

    root.mainloop()

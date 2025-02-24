import tkinter as tk
import subprocess
import sys
import os
from main import main

# Use this path to locate bundled files like 'main.py'
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        # If running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def start_game():
    # Construct full path to main.py in the bundle
    main_script = resource_path("main.py")
    subprocess.run(["python", main_script])
    # This ensures 'main.py' will be executed correctly

# Create the main GUI window
root = tk.Tk()
root.title("Asteroids Launcher")

# Add a Start button
start_button = tk.Button(root, text="Start Game", command=start_game, height=3, width=20)
start_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()

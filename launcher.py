import tkinter as tk
import os
import sys
import time
import subprocess
from threading import Thread
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from main import main


# def initialize_pygame(embed):
#   """Initialize pygame and start the game loop."""
#   # Set SDL environment to use the tkinter frame
#   os.environ["SDL_VIDEODRIVER"] = "cocoa"  # Appropriate driver for macOS (cocoa)
#   os.environ["SDL_WINDOWID"] = str(embed.winfo_id())  # Embed pygame into tkinter

#   print("Embedding into window ID:", os.environ["SDL_WINDOWID"])  # Debugging output
#   time.sleep(0.5)

#   # Initialize pygame
#   import pygame
#   pygame.display.init()
#   # segmentation error with init
#   pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#   # Start the pygame main loop on a separate thread
#   game_thread = Thread(target=main)
#   game_thread.daemon = True  # Ensures the thread exits when tkinter exits
#   game_thread.start()


# def start_game():
#   """Create the tkinter frame and initialize pygame after idle."""
#   # Create an embedded frame for pygame inside tkinter
#   embed = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Adjust to your screen size
#   embed.pack(pady=20)  # Add padding or place where desired
#   embed.update()  # Make sure tkinter realizes the frame

#   # Use after_idle to initialize pygame when tkinter's event loop is idle
#   root.after_idle(initialize_pygame, embed)


def resource_path(relative_path):
  if hasattr(sys, "_MEIPASS"):
    # If running as a PyInstaller bundle
    resources_dir = os.path.abspath(os.path.join(sys._MEIPASS, "..", "Resources"))
    return os.path.join(resources_dir, relative_path)
  return os.path.abspath(relative_path)


def start_game():
  # Construct full path to main.py in the bundle
  main_script = resource_path("main.py")
  print("running main from ", main_script)
  # This ensures 'main.py' will be executed correctly
  try:
        process = subprocess.Popen([sys.executable, main_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
  except Exception as e:
      print("Error starting game:", e)


def quit_launcher():
  """Properly quit the application."""
  root.quit()
  root.destroy()
  sys.exit()


# Create the main tkinter window
root = tk.Tk()
root.title("Asteroids")
root.geometry(f"{SCREEN_WIDTH // 2}x{SCREEN_HEIGHT // 2}")  # Adjust to add space for your buttons and the pygame frame

# Add a welcome/game status label
game_label = tk.Label(root, text="Asteroids Launcher", font=("Arial", 14))
game_label.pack(pady=10)

# Add a "Start Game" button
start_button = tk.Button(root, text="Start Game", command=start_game, height=3, width=20)
start_button.pack(pady=20)

# Add a "Quit" button
quit_button = tk.Button(root, text="Quit", command=quit_launcher, height=2, width=15)
quit_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()

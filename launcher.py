import tkinter as tk
import subprocess

def start_game():
    # Run the game as an external process so the GUI remains active
    # Replace 'path_to_game' with the path to your main game entry file
    subprocess.run(["python", "main.py"])
    # Game will run in this subprocess, and when it exits, you can restart from the GUI

# Create the main GUI window
root = tk.Tk()
root.title("Asteroids Launcher")

# Add a Start button
start_button = tk.Button(root, text="Start Game", command=start_game, height=3, width=20)
start_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()

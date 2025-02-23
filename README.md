# Asteroids game

Asteroids-inspired game built with Pygame, demonstrating OOP principles and basic game mechanics. Based on the guided project by [Boot.Dev](https://www.boot.dev/).

Project manager kept giving me sticky notes with update requests so I forced him to create his own GitHub and submit issues there instead. (Kids can be tyrants)

## Enhancements

- Enhanced background...should look like you're in space, right? Also displays your current score
- Player enhancements and upgrades:
  - added wrapping so you don't drift into the void
  - enhanced control surface options for easier movement
  - upgraded ship visuals from basic triangle to level-based image overlay
  - introduced leveling system to enhance visuals and weapon (shots) based on score
- Asteroid visual upgrades: now spinning, randomly shaped polygons instead of basic circles
- End screen loop that allows game replay without restarting the script
- Added launcher window with start button
- Fixed Overflow Error: previously, offscreen entities weren't removed and kept updating until overflow
- Added boss level that appears based on player level, including a character chase mechanic
- \[WIP\] Packaged executable: No more command line launching! (MacOS first, Windows support planned)

## Local Usage

### Prerequisites

Ensure you have **Python 3.13.1** or later installed.
Check your Python version with:

```bash
python --version
```

### Installation Steps

1. Clone the repository and navigate into it:

   ```bash
   git clone https://github.com/JonathanCrider/asteroids.git
   cd asteroids
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows (Command Prompt):

     ```cmd
     venv\Scripts\activate
     ```

   - On Windows (PowerShell):

     ```powershell
     venv\Scripts\Activate.ps1
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Play!

You can run the game directly if you want, or you can use the launcher.

```bash
python3 main.py
```

-- OR --

```bash
python3 launcher.py
```

### Controls

Movement:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>W</kbd>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- OR --&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>↑</kbd> \
<kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>←</kbd> <kbd>↓</kbd> <kbd>→</kbd>

Fire shot:

<kbd>Space</kbd> -- OR -- <kbd>⏎ Return</kbd> -- OR -- <kbd>⏎ Numpad Enter</kbd>

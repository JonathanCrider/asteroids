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
- Added boss level that appears based on player level, including a character chase mechanic and health-based visuals
- Packaged executable: No more command line launching! (see below)
  - *macOS only, Windows support planned*

## Install

macOS only: [click here to download](https://drive.google.com/file/d/14ZQ4nNw7SEzKzvQYVxIkAf4-Dy6XBFOd) the `.dmg`, then drag/drop the file into your Applications folder.

It's not signed, so you will need to do the following to open it on your machine:

### Option A

1. Right-click the app → Open.
2. macOS will show a warning, but this time it will allow you to click Open.

### Option B

On more recent versions of macOS, you may need to approve it from System Settings -> Privacy & Security:

1. **Try opening the app**  
   - Double-click the `Asteroids.app` inside the `Asteroids-Launcher.dmg`.  
   - If macOS blocks it with the error, **close the message**.

2. **Go to System Settings → Privacy & Security**  
   - Click **Apple Menu**  → **System Settings** → **Privacy & Security**.  
   - Scroll down to the **Security** section.

3. **Find the blocked app**  
   - Under `"App was blocked from use because it is not from an identified developer"`, click **"Allow Anyway"**.

4. **Open the app again**  
   - Now, **right-click** the app and select **Open**.  
   - A new prompt appears, but this time, there's an option to **Open**.

## Play!

### Movement

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>W</kbd>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- OR --&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>↑</kbd> \
<kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<kbd>←</kbd> <kbd>↓</kbd> <kbd>→</kbd>

Note: <kbd>A</kbd> and <kbd>D</kbd> are for strafing!

### Firing

<kbd>Space</kbd> -- OR -- <kbd>⏎ Return</kbd> -- OR -- <kbd>⏎ Numpad Enter</kbd>

## Local Development

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

### Running Locally

Navigate to the root directory and run the following command:

```bash
python launcher.py
```

# Asteroids game

Asteroids-inspired game built with Pygame, demonstrating OOP principles and basic game mechanics. Based on the guided project by [Boot.Dev](https://www.boot.dev/).

My project manager kept giving me sticky notes with update requests so I forced him to create his own GitHub and submit issues there instead. Kids can be demanding sometimes :)

## Enhancements

The base project is a great start, but very simple. I've added several of my own enhancements.

### UI/UX

- Enhanced background...should look like you're in space, right? Also displays your current score and accuracy
- Asteroid visuals, upgraded simple circle to a random polygon with rotation
- Player graphical image overlay
- Added additional control options, including strafing
- End screen loop that allows game replay without restarting the game
- Added launcher window with start and quit buttons
  - Now includes semi-hidden test button, so you can traverse the level quickly to see all the improvements
- Sounds!

### Logic

- Player location wrapping, so you don't drift into the void
- Player leveling, based on your score. Includes visual updates and weapon upgrades
- Added boss level that appears based on player level, including a character chase mechanic and health-based visuals
- Global config to enable testing (reduces level/upgrade thresholds) without modifying code

### Bug Fixes

- Fixed Overflow Error: previously, offscreen entities weren't removed and kept updating until overflow error crashed the game

### Known Issues

- Random line flashes. Probably a rounding/draw error somewhere

### Installable

- Packaged executable: No more command line launching! (see below)
  - *macOS only, Windows support planned*

## Install

macOS only: [click here to download](https://drive.google.com/file/d/14ZQ4nNw7SEzKzvQYVxIkAf4-Dy6XBFOd) the `.dmg`, then drag/drop the file into your Applications folder.

It's not signed, so you will need to allow MacOS to bypass some of the security warnings.

As always, please use caution and common sense when installing unknown applications on your machine.

1. **Try opening the app**  
   - Double-click the `Asteroids.app` inside the `Asteroids-Launcher.dmg`.  
   - If macOS blocks it with the error, **close the message**.

2. **Go to System Settings → Privacy & Security**  
   - Click **Apple Menu**  → **System Settings** → **Privacy & Security**.  
   - Scroll down to the **Security** section.

3. **Find the blocked app**  
   - Under `"App was blocked from use because it is not from an identified developer"`, click **"Allow Anyway"**.
   - If you don't find this option, you probably have an older version of MacOS, so step 4 should work without this.

4. **Open the app again**  
   - Now, **right-click** the app and select **Open**.  
   - A new prompt appears, but this time, there's an option to **Open**.

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

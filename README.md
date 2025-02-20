# Asteroids game

Simple asteroids-inspired game built with pygame, based on the guided project by [Boot.Dev](https://www.boot.dev/).

The project demonstrates OOP principles and basic game mechanics.

## Enhancements

- Player wrapping: Instead of infinte travel offscreen (until you find the Overflow value), your ship wraps to the other side of the screen
- Player visuals: Enhanced visual distinction between player, shots, and asteroids
- Background: Enhanced background...should look like you're in space, right?
- Score: Added scoring mechanic and persistant visual display of current score
- End screen: Game over screen before exit
- Fixed `Overflow Error`: This occurs because when entities are created, they are not removed when offscreen, especially shots
- \[WIP\] Packaged executable: So you don't have to launch from the command line (MacOS first, we'll see about Windows)

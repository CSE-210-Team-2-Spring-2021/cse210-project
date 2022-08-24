# Definitely Not a Sinistar Clone

Your goal in Sinistar is simple: destroy asteroids to get a high score. There are laser bots sent to destroy you and you must evade their attacks.

Crystals don't start out floating in space; originally, they are buried deep with the Planetoids drifting through space around you. They can be broken loose (or mined) by firing into the Planetoids. Workers can't mine crystals themselves, so they wait for you to do it and then try to steal the crystals before you can get to them. You'll want to prevent the Workers from stealing crystals for two reasons:

1. The crystals you collect are converted to Sinibombs
2. Using Sinibombs earns you extra points and prevents asteroids from splitting

## Getting Started

---

Make sure you have Python 3.8.0 or later and arcade 2.6.0 or new installed
and running on your machine. You can install arcade by opening a terminal
and running the following command.

```
python3 -m pip install arcade
```

After you've installed the required libraries, open a terminal and browse to the
project's root folder, this folder is named Sinistar as is found at ~\cse210-project-main\cse210-project-main\project_template\Sinistar. Start the program by executing the __main__.py. I recommend running this is an IDE to ensure it is properly running. Details below

You can also run the program from an IDE like Visual Studio Code. Start your IDE
and open the project folder. Select the main module inside the hunter folder and
click the "run" icon.

## Project Structure

---

The project files and folders are organized as follows:

```
project_template        (project root folder)
+-- docs                (project documentation)
+-- Sinistar              [src code files - rename for project]
  +-- assets            (program asset files)
  +-- data              (program data files)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- LICENSE             (license file)
+-- README.md           (general info)
```

## Required Technologies

---

Python 3.9.5
Python Arcade Library

## Authors

---

Nathaniel Jackson - jac20003@byui.edu - drbubbles40-school -Mostly contributed to sinistarwindow.py, windowhelper.py, menu.py, and small portions of most other classes.
Kyle Ames - ame18007@byui.edu
TJ Anderson - and15126@byui.edu
Chase Patterson - pat20001@byui.edu

## Sound and Sprite Credits

---

In-Game Theme: https://www.bensound.com
Enemy Laser Sound: https://www.soundfishing.eu
Laser Sound: https://www.findsounds.com
Crystal Sound: https://kenney.nl/assets/impact-sounds
Asteroid sprite: https://www.vippng.com/preview/ixJwwhh_clipart-transparent-background-asteroid-png/
Bomb launch effect: https://www.findsounds.com
Crystal Pickup: https://mixkit.co/free-sound-effects/sci-fi/

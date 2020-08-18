# PianoTiles- Bot

## Where to play
To play the game visit...

[Piano-Tiles](http://tanksw.com/piano-tiles/)

Change the co-ordinates accordingly.

## How does the bot work

1. The pixel values of each column obtained
2. They are compared to the colour of the box
3. We move the mouse there and click it

## Statistics

I figured out that using win32 , I ws able to click considerably
fast compared to `pyautogui.click()` function.

Approximately the script takes 100 screen shots a second
and can also click at almost the same rate..

The bottleneck is the speed of the image being taken...
If you have any ideas feel free to modify the code.

## How to use

1. Change the co-ordinates as mentioned in the code
2. Press q on the keyboard to start the script
3. It waits for 2 seconds before clicking initially
4. Press q again to exit code execution

## Some Highscores

[Arcade Mode](docs/CONTRIBUTING.md)

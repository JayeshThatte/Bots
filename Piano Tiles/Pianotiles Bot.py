# We import keyboard so that we can find which key is pressed.
# We use pyautogui to detect pixel and take screenshot.
# Time module is used to sleep between 2 events.
# win32api & win32con are used to click the mouse at very fast rates.

"""
To play the game visit...
http://tanksw.com/piano-tiles/

Change the co-ordinates accordingly.

"""

import keyboard
import pyautogui
from time import sleep
import win32api
import win32con


def click(x, y):
    """ We use this function to click at a specifed
    x and a y position . x=0,y=0 at top left point in the screen """

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    # This pauses the script for 0.01 seconds.
    # We need to have this delay else clicks fail to execute.

    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


"""

while True:
    pyautogui.displayMousePosition()

"""

# The above piece of code is used to identify the constants in the program.
# The y co-ordinates are constant throughout

# START_BOX_Y is the Start button y co-ordinates.
START_BOX_Y = 548
# CLICK_BOX_Y is the Tile Button y co-ordinates.
CLICK_BOX_Y = 400
# COLOUR_TILE is the colour of each tile.
COLOUR_TILE = (17, 17, 17)


# This is a temporary loop which allos further execution only
# after 'q' is pressed

while keyboard.is_pressed('q') == False:
    continue

sleep(2)

# The below code is required to click the initial start button.
# I concluded that the column in pianotile game changes every 70 pixel in x - axis.

for i in range(560, 800, 70):
    if pyautogui.pixel(i, START_BOX_Y) == COLOUR_TILE:
        click(i, START_BOX_Y)

# To quit the program we press 'q'
while keyboard.is_pressed('q') == False:

    for i in range(560, 800, 70):
        if pyautogui.pixel(i, CLICK_BOX_Y) == COLOUR_TILE:

            # We break loop after a click as it saves time
            # and only 1 black box exists each row.

            click(i, CLICK_BOX_Y+30)
            break

#! python3

# Library
import pyautogui # pip3 install pyautogui

screenWidth, screenHeight = pyautogui.size()

while True:
    # locate the accept button
    accept = pyautogui.locateOnScreen('./img/accept.png')

    if accept:
        pyautogui.click(x=screenWidth/2, y=screenHeigh/2, button='left')

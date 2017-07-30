#! python3

# Library
import pyautogui # pip3 install pyautogui

while True:
	# set accept to be 0
	accept = 0
	# locate the accept button
	accept = pyautogui.locateCenterOnScreen('./img/accept.png')

	if not (accept is None):
		pyautogui.click(accept[0],accept[1])
		print("Accept btn pressed")

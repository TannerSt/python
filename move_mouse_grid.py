import os
import keyboard
import mouse
import time
from time import sleep

def mouse_snap_move():
		keyboard.press("ctrl")
		sleep(.2)
		mouse.click("left")
		keyboard.release("ctrl")

def transmute():

	def my_pixel_range(start, end, step):
		while start <= end:
			yield start
			start += step


	for x in my_pixel_range(1200, 1466, 38):
		mouse.move(x, 542, absolute=True, duration=0.2)
		mouse_snap_move()
		sleep(0.2)

		mouse.move(0, 34, absolute=False, duration=0.2)
		mouse_snap_move()
		sleep(0.2)

		mouse.move(0, 34, absolute=False, duration=0.2)
		mouse_snap_move()
		sleep(0.2)

		mouse.move(0, 34, absolute=False, duration=0.2)
		mouse_snap_move()
		sleep(0.2)

		mouse.move(620, 570, absolute=True, duration=0.2)
		sleep(0.2)
		mouse.click("left")
		sleep(0.5)
		mouse.move(656, 518, absolute=True, duration=0.2)
		sleep(0.2)
		mouse_snap_move()
		sleep(0.2)


sleep(5)
transmute()
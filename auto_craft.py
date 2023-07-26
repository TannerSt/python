import keyboard
import mouse
import time
from time import sleep
import os
#importing subprocess to run an .exe
import subprocess
#importing Popen to send keyboard commands within subprocess via a PIPE
from subprocess import Popen, PIPE
#importing shutil to copy files
import shutil


###specify the character name, make sure they are in the first slot on char select###
character="ama"

###loops the whole script n(end) times, filling stash tab 1 when n=12###
def crafting_run_range(start, end, step):
	while start <= end:
		yield start
		start += step

for x in crafting_run_range(1, 11, 1):
	


	#with statement to allow subprocess to run as process, stdin for piping script commands
	###this chunk literally plays Diablo 2 based on static elements in game###
	with subprocess.Popen(
		["C:\Program Files (x86)\Diablo II Resurrected\D2R.exe"], stdin=subprocess.PIPE
	) as process:

		def press_any_Key():
			keyboard.send("esc")

		def select_play():
			mouse.move(950, 830, absolute=True, duration=0.2)
			mouse.click("left")
			mouse.move(960, 500, absolute=True, duration=0.2)
			mouse.click("left")

		def open_cube():
			keyboard.send("b")
			mouse.move(1160, 630, absolute=True, duration=0.2)
			mouse.click("right")



		def mouse_snap_move():
			keyboard.press("ctrl")
			sleep(.2)
			mouse.click("left")
			keyboard.release("ctrl")

		def open_share_stash():
			press_any_Key()
			sleep(0.2)
			mouse.move(790, 410, absolute=True, duration=0.2)
			sleep(0.2)
			mouse.click("left")
			mouse.move(576, 264, absolute=True, duration=0.2)
			sleep(0.2)
			mouse.click("left")

		def transmute():

			def my_pixel_range(start, end, step):
				while start <= end:
					yield start
					start += step

			def column_bump():
				mouse.move(0, 34, absolute=False, duration=0.2)
				mouse_snap_move()
				sleep(0.2)


			for x in my_pixel_range(1200, 1466, 38):
				mouse.move(x, 542, absolute=True, duration=0.2)
				mouse_snap_move()
				sleep(0.2)

				column_bump()
				column_bump()
				column_bump()

				mouse.move(620, 570, absolute=True, duration=0.2)
				sleep(0.2)
				mouse.click("left")
				sleep(0.5)
				mouse.move(656, 518, absolute=True, duration=0.2)
				sleep(0.2)
				mouse_snap_move()
				sleep(0.2)


		def items_to_stash():

			

			def my_crafted_item_range(start, end, step):
				while start <= end:
					yield start
					start += step

			for x in my_crafted_item_range(1200, 1466, 38):
				mouse.move(x, 644, absolute=True, duration=0.2)
				mouse_snap_move()
				sleep(0.2)

		def exit_game():
			press_any_Key()
			sleep(1)
			mouse.move(950, 472, absolute=True, duration=0.2)
			mouse.click("left")
			sleep(1)
			press_any_Key()
			mouse.move(845, 546, absolute=True, duration=0.2)
			sleep(2)
			mouse.click("left")



	#note this must be running in 1280x800 windowed mode to work for these mouse inputs
	###the script###
		sleep(4)

		press_any_Key()
		sleep(4)
		press_any_Key()
		sleep(4)
		press_any_Key()
		sleep(6)

		select_play()
		sleep(6)

		open_cube()
		sleep(0.2)

		transmute()
		sleep(0.2)

		open_share_stash()
		sleep(0.2)

		items_to_stash()
		sleep(0.2)

		press_any_Key()
		sleep(0.2)

		exit_game()
		sleep(5)


	def restore_character():
		source = r"C:\Users\tsain\Diablo2Saves"
		destination = r"C:\Users\tsain\Saved Games\Diablo II Resurrected"

		for file in os.listdir(source):
			if str(character) in file.lower():#specify str or it wont match shit

				if not os.path.exists(destination):
					os.makedirs(destination)

				shutil.copy2(os.path.join(source, file), os.path.join(destination, file))

	sleep(4)
	restore_character()
	sleep(8)

	print(str(x)+"runs complete")
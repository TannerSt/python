#shitty script to copy any character save to temp location

import os
import shutil


#using for/if statement to grab any file that starts with Amazon so I can reduce number of lines

char = input("Which Character?: ")
print("Copying", char)

source = r"C:\Users\tsain\Saved Games\Diablo II Resurrected"
destination = r"C:\Users\tsain\Diablo2Saves"

for file in os.listdir(source):
	if str(char) in file.lower():#specify str or it wont match shit

		if not os.path.exists(destination):
			os.makedirs(destination)

		shutil.copy2(os.path.join(source, file), os.path.join(destination, file))
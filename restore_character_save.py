#shitty script to restore character to keep imbueing or crafting, must have base item or items on her person

import shutil
import os


#using for/if statement to grab any file that starts with Amazon so I can reduce number of lines

char = input("Which Character?: ")
print("restored save for", char)

source = r"C:\Users\tsain\Diablo2Saves"
destination = r"C:\Users\tsain\Saved Games\Diablo II Resurrected"

for file in os.listdir(source):
	if str(char) in file.lower():#specify str or it wont match shit

		if not os.path.exists(destination):
			os.makedirs(destination)

		shutil.copy2(os.path.join(source, file), os.path.join(destination, file))
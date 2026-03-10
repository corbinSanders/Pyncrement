import configparser
import os
import pynput
from pynput import keyboard


class IncFile:
	filename = ""

	def __init__(self, filename):
		print("Trying to open " + filename)
		if os.path.isfile(filename):
			print ("File open success!")
			self.filename = filename
		else:
			raise Exception("File cannot be found. Ensure config.ini has correct file.")

	def incOrDec(self, action):
		with open(self.filename, 'r+') as file:
			number = int(file.read().strip())

			if action=='I':
				new_number = number+1
			elif action=='D' and number!=0:
				new_number = number-1
			else:
				return
			file.seek(0)
			file.write(str(new_number))
			file.truncate()

	def inc(self):
		self.incOrDec('I')

	def dec(self):
		self.incOrDec('D')

def exit():
	raise keyboard.Listener.StopException


def main():
	print("Welcome")
	config = configparser.ConfigParser()
	config.read("config.ini")

	increment_file = config["SCRIPT"]["increment_file"]
	increment_keystroke = config["SCRIPT"]["increment_keystroke"]
	decrement_keystroke = config["SCRIPT"]["decrement_keystroke"]
	exit_keystroke = config["SCRIPT"]["exit_keystroke"]

	incFile = IncFile(increment_file)

	with keyboard.GlobalHotKeys({
		increment_keystroke: incFile.inc,
		decrement_keystroke: incFile.dec,
		exit_keystroke: exit
		}) as h:
		h.join()



main()




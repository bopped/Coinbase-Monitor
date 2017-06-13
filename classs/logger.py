# logger.py
# developer: @eggins

import time, sys

class logger:

	# initalise base variable structure
	def __init__(self):
		# setting an array of colours to be used
		self.colours = {
			"error" 		: "\033[91m",
			"success" 		: "\033[92m",
			"info" 			: "\033[96m",
			"debug" 		: "\033[95m",
			"yellow" 		: "\033[93m",
			"lightpurple" 		: "\033[94m",
			"lightgray" 		: "\033[97m",
			"clear"			: "\033[00m"
		}

	def log(self, message="", color="", file="", shown=True, showtime=True, nocolor=""):
		# define the current time when calling the logger as HOUR:MINUTE:SECOND
		currentTime = time.strftime("%H:%M:%S")

		# define which colour is being used
		try:
			colourString = self.colours[color]
		except:
			colourString = ""

		# construct time string
		if showtime:
			timestring = "[%s] " % currentTime
		else:
			timestring = ""

		# path together the message and the clear colour
		messageString = message + self.colours['clear']
		noColourString = message

		# if there is text in the "nocolor" field
		# add : and paste the content afterward
		if nocolor:
			messageString += ": %s" % nocolor 
			noColourString += ": %s" % nocolor 

		# determine the final string to be printed and logged to file
		finalString = "%s%s%s\n" % (timestring, colourString, str(messageString))
		noColourFinalString = "%s%s\n" % (timestring, str(noColourString))

		# print from the system to the terminal
		# this method helps stop overlap when threading
		sys.stdout.write(finalString)
		sys.stdout.flush()

		# print message to file if requested
		if file:
			with open(file, "a") as f:
				f.write(noColourFinalString)

	def overwriteLine(self, msg='', new_line=True):

		currentTime = time.strftime("%H:%M:%S")

		if new_line:
			msg += '\n'
			sys.stdout.write('%s' % (msg))

			sys.stdout.flush()
			return True
		
		elif msg != '':
			sys.stdout.write('[%s] %s' % (currentTime, msg))

		sys.stdout.flush()

	def returnLine(self):
		sys.stdout.write('\r')
		sys.stdout.flush()

"""
Program: numberFieldDemo.py
Chapter 8 (Page 264)
1/22/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Example of a GUI-based app which has labels, numeric fields for both input and output and a command button. Command button triggers a ???
"""

from breezypythongui import EasyFrame
import math
# Other imports go here

# Class header (class name will change project to project)
class NumberFieldDemo(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Square Root Calculator", width = 280, height = 160, background = "hotpink")

		# Label and entry field for the input
		self.addLabel(text = "An integer", row = 0, column = 0, background = "hotpink", foreground = "white")
		self.inputField = self.addIntegerField(value = 0, row = 0, column = 1, width = 10)
		self.inputField["background"] = "azure"

		# Label and entry field for the output
		self.addLabel(text = "Sqaure Root", row = 1, column = 0, background = "hotpink", foreground = "white")
		self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, state = "readonly", width = 10, precision = 2)

		# The command button which triggers the convert() function
		self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computerSqrt)

	# Definition of the convert() function
	def computerSqrt(self):
		""" Collects the input integer, calculates the square root and outputs the result."""
		try:
			number = self.inputField.getNumber()
			result = math.sqrt(number)
			self.outputField.setNumber(result)
		except ValueError:
			self.messageBox(title = "ERROR!", message = "Input MUST be an integer greater than or equal to zero!")

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	NumberFieldDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()
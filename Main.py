# This file is an example of your existing project. You can import the TypewriterEffect file and call its functions in order to use it.
from TypewriterEffect import *

# String Variables
message = "Hello, this is a typewriter test! \nThis is another line. \nYou can call this function any time to make cool projects."
message2 = "\nTesting testing... \nNew line."

# Function Calling (Main Program).
typewriter(message) # Call the typewriter function and display the string variable 'message' with the default typing speed and settings.
typewriter(message2, 0.2, 2) # Displays the string variable 'message2' with the typing speed set to 0.2 and the speed of the new line delay set to 2.

time.sleep(1)
clear_message() # Call the clear_message function. This is optional if you want it.

time.sleep(1)
exit = input("Press Enter to Exit...")
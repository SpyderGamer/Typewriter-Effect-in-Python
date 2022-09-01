import sys
import time
import os
from os import name

# This is the main program's function, call it and provide parameters to customize it as you like.
def typewriter(say, message_speed = 0.1, new_line_delay_time = 1):
    for character in say:
        sys.stdout.write(character)
        sys.stdout.flush()
        
        if character != "\n":
            time.sleep(message_speed)
        else:
            time.sleep(new_line_delay_time)

# Call this function to clear the screen (Clear commands are based on you Operating System). 
def clear_message():
    if name == "nt":
        # For Windows
        os.system("cls")
    else:
        # For Mac and Linux (Here, os.name is 'posix')
        os.system("clear")
# in ter terminal write help
# access the terminal and write modules. all modules will be listed.
#type list to see all available functions/modules
# click Q to quit the program

import math                   # import a module called math
print("Math Module: ",math.__doc__)     # docstring of math module

# use . to call specific function from imported module
pi = math.pi                # assign value of pi from math module to variable pi
print("\nValue of Pi:\t",pi)    # prints Value of Pi:

def main():
    """
    This is a simple program that demonstrates how to use the GPIO pins on Raspberry Pi for input and output purposes.
    The LED connected to pin 17 will light up when you press the button connected to pin 23 (GPIO 04).
    After pressing the button, it will turn off after another button press.
    """
    try:
        print("""\nWelcome to the Raspberry Pi IOT Shield Demo!
              This demo shows how to control an LED using a pushbutton switch.
              Press Ctrl+C to exit.\n""")
        while True:
            if check_switch():     # Checks if the switch is pressed
                set_leqd(ON)         # If so, turns ON the LED
            else:                   # If not, keeps checking until released
                pass             # Do nothing - just wait for next loop iteration
    except KeyboardInterrupt:      # If user hits Ctrl+C
        cleanup()       # Turn OFF the LED before leaving

if __name__ == '__main__':
    main()


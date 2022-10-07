from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
import sys


print("LED Signaler...by kevinc\n")
print("Press ENTER to signal LED controller...")

# myLED = LED(17)

# def say_hello():
#     print("Hello!")

# button = Button(2)
# # button.when_pressed = say_hello

# button.when_pressed = myLED.on
# button.when_released = myLED.off

# pause()

while True:
     # input
    string = str(input())
  
    sys.stdout.write("Signaling LED controller...")
    
    # TODO really send signal and remove this sleep.
    sleep(1)

    print("DONE")
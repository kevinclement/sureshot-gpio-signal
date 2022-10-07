from gpiozero import OutputDevice
from time import sleep
import sys

print("LED Signaler...by kevinc\n")
print("Press ENTER to signal LED controller...")

# GPIO pin hooked up to LED controller
device = OutputDevice(17)

while True:
     # block on input
     string = str(input())
     sys.stdout.write("Signaling LED controller...")

     # send HIGH signal over GPIO to controller
     device.on()

     # leave it HIGH for 300ms
     sleep(.3)

     # turn it off
     device.off()

     print("DONE")
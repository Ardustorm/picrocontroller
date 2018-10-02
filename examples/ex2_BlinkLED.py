import boardfuncs
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"


#setup board comunication
bf = boardfuncs.BoardFuncs()

#set LED pins to output mode (general purpose input output push pull)
bf.setPinMode(LEDPin1, boardfuncs.GPIO_PP)
bf.setPinMode(LEDPin2, boardfuncs.GPIO_PP)

#print to user
print("Blinking LED")
while True:
    #toggle both pins
    bf.togglePin(LEDPin1)
    bf.togglePin(LEDPin2)
    #wait 1/2 second
    time.sleep(.5)

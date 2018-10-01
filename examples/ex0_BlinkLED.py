import boardfuncs
import time

#define pin names to use
pin1 = "PB12"
pin2 = "PC13"


#setup board comunication
bf = boardfuncs.BoardFuncs()

#set LED pins to output mode (general purpose input output push pull)
bf.setUpPin(pin1, boardfuncs.GPIO_PP)
bf.setUpPin(pin2, boardfuncs.GPIO_PP)

#print to user
print("Blinking LED")
while True:
    #toggle both pins
    bf.togglePin(pin1)
    bf.togglePin(pin2)
    #wait 1/2 second
    time.sleep(.5)
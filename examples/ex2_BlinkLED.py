import picro
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"

def setup():
    #set LED pins to output mode (general purpose input output push pull)
    myRobot.setPinMode(LEDPin1, picro.GPIO_PP)
    myRobot.setPinMode(LEDPin2, picro.GPIO_PP)

def loop():
    #print to user
    print("Blinking LED")
    while True:
        #toggle both pins
        myRobot.togglePin(LEDPin1)
        myRobot.togglePin(LEDPin2)
        #wait 1/2 second
        time.sleep(.5)

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup,loop)

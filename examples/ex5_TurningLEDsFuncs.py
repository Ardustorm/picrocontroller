import picro
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"

#states are defined at top  
 def straight():
    #set leds, set time till next state, increment state count, and set next state
    myRobot.setPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    doneTime = time.time() + 3
    stateCount += 1
    if(stateCount == 1 or stateCount == 7):
        nextState = right
    else:
        nextState = left


def right():
    #set leds, set time till next state, increment state count, and set next state
    myRobot.clearPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    doneTime = time.time() + 1.5
    stateCount += 1
    nextState = straight


def left():
    #set leds, set time till next state, increment state count, and set next state
    myRobot.setPin(LEDPin1)
    myRobot.clearPin(LEDPin2)
    doneTime = time.time() + 1.5
    stateCount += 1
    nextState = straight

#def state varibles after state defs
stateCount = 0
nextState = straight
doneTime = 0

def setup():
    #set LED pins to inputs
    myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
    myRobot.setPinMode(LEDPin2, picro.GPIO_IN)
    
    #print to user
    print("Starting Turning State Machine")

def loop():
    #check if timer is done
    if(time.time() >= doneTime):
        nextState()        

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)
        
        
        
        
        
        
        

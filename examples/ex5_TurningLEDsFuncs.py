import picro
import time

#define pin names to use
LEDPin1 = "PA4"
LEDPin2 = "PA5"

#states are defined at top  
def straight():
    #declare varibles you will update in this method
    global nextState
    global stateCount
    global doneTime
    
    #set leds, set time till next state, increment state count, and set next state
    myRobot.setPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    doneTime = time.time() + 3
    stateCount += 1
    if(stateCount == 1 or stateCount == 7):
        nextState = right
    elif(stateCount == 3 or stateCount == 5):
        nextState = left
    else:
        print("Final State")
        nextState = done

def right():
    #declare varibles you will update in this method
    global nextState
    global stateCount
    global doneTime
    
    #set leds, set time till next state, increment state count, and set next state
    myRobot.clearPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    doneTime = time.time() + 1.5
    stateCount += 1
    nextState = straight

def left():
    #declare varibles you will update in this method
    global nextState
    global stateCount
    global doneTime
    
    #set leds, set time till next state, increment state count, and set next state
    myRobot.setPin(LEDPin1)
    myRobot.clearPin(LEDPin2)
    doneTime = time.time() + 1.5
    stateCount += 1
    nextState = straight

def done():
    myRobot.clearPin(LEDPin1)
    myRobot.clearPin(LEDPin2)

#def state varibles after state defs
nextState = straight
stateCount = 0
doneTime = 0

def setup():
    #set LED pins to inputs
    myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
    myRobot.setPinMode(LEDPin2, picro.GPIO_IN)
    
    #print to user
    print("Runnig LED State Machine")

def loop():
    #declare varibles you will update in this method
    global doneTime
    
    #check if timer is done
    if(time.time() >= doneTime):
        nextState()        

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)
        
        
        
        
        
        
        

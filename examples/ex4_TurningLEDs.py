import picro
import time

#define pin names to use
LEDPin1 = "PA4"
LEDPin2 = "PA5"

#def state vars
currentState = 0
doneTime = 0

#def states of LEDS
def straight():
    myRobot.setPin(LEDPin1)
    myRobot.setPin(LEDPin2)

def right():
    myRobot.clearPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    
def left():
    myRobot.setPin(LEDPin1)
    myRobot.clearPin(LEDPin2)

def stop():
    myRobot.clearPin(LEDPin1)
    myRobot.clearPin(LEDPin2)

def setup():
    #set LED pins to inputs
    myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
    myRobot.setPinMode(LEDPin2, picro.GPIO_IN)
    
    #print to user
    print("Running LED State Machine")

def loop():
    #declare varibles you will update
    global doneTime
    global currentState
    
    #check if timer is done
    if(time.time() >= doneTime):
        
        #if the current state is even
        if(currentState >= 9):
            #if done stop
            stop()
        elif(currentState%2 == 0):
            #go straight, set timer, and increment state
            straight()
            doneTime = time.time() + 3
            currentState += 1
        elif(currentState == 1 or currentState == 7):
            #go right, set timer, and increment state
            right()
            doneTime = time.time() + 1.5
            currentState += 1
        elif(currentState == 3 or currentState == 5):
            #go left, set timer, and increment state
            left()
            doneTime = time.time() + 1.5
            currentState += 1

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)
        
        
        
        
        
        
        

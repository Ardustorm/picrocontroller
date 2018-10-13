import picro
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"

curentState = 0
doneTime = 0

def setup():
    
    #set LED pins to inputs
    myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
    myRobot.setPinMode(LEDPin2, picro.GPIO_IN)
    
    #print to user
    print("Starting Turning State Machine")

def straight():
    myRobot.setPin(LEDPin1)
    myRobot.setPin(LEDPin2)


def right():
    myRobot.clearPin(LEDPin1)
    myRobot.setPin(LEDPin2)
    
def left():
    myRobot.setPin(LEDPin1)
    myRobot.clearPin(LEDPin2)

def loop():
    #check if timer is done
    if(time.time() >= doneTime):
        
        #if the current state is even
        if(currentState%2 == 0):
            #go straight and set timer
            straight()
            doneTime = time.time() + 3
        elif(curentState == 1 or currentState == 7):
            #go right and set timer
            right()
            doneTime = time.time() + 1.5
        elif(curentState == 3 or currentState == 5):
            left()
            doneTime = time.time() + 1.5
        #always increment state when timer runs out
        currentState += 1

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)
        
        
        
        
        
        
        

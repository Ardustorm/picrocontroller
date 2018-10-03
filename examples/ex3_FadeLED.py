import picro
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"
PWMPin1 = "PA1"

def setup():
    
    #set LED pins to inputs
    myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
    myRobot.setPinMode(LEDPin2, picro.GPIO_IN)
    
    #init PWM pin clock freq (Hz)
    myRobot.initPWM(PWMPin1, 1000)
    
    #print to user
    print("Fading LED")

def loop():
    i = 10000
    while i > 0:
        #set duty cycle of PWM pin 0-10000
        myRobot.setPWM(PWMPin1, i)
        #delay for 1/10 of a second
        time.sleep(.1)
        i -= 1000
    while i < 10000:
    #set duty cycle of PWM pin 0-10000
        myRobot.setPWM(PWMPin1, i)
        #delay for 1/10 of a second
        time.sleep(.1)
        i += 1000

if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)
        
        
        
        
        
        
        

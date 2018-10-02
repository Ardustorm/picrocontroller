import boardfuncs
import time

#define pin names to use
LEDPin1 = "PB12"
LEDPin2 = "PC13"
PWMPin1 = "PA1"

#setup board comunication
bf = boardfuncs.BoardFuncs()

#set LED pins to inputs
bf.setPinMode(LEDPin1, boardfuncs.GPIO_IN)
bf.setPinMode(LEDPin2, boardfuncs.GPIO_IN)

#init PWM pin clock freq (Hz)
bf.initPWM(PWMPin1, 1000)

#print to user
print("Fading LED")
i=10000
while True:
    while i > 0:
        #set duty cycle of PWM pin 0-10000
        bf.setPWM(PWMPin1, i)
        #delay for 1/10 of a second
        time.sleep(.1)
        i -= 1000
    while i < 10000:
    #set duty cycle of PWM pin 0-10000
        bf.setPWM(PWMPin1, i)
        #delay for 1/10 of a second
        time.sleep(.1)
        i += 1000

        
        
        
        
        
        
        
        

import boardfuncs
import time


def TestBoardFuncsValidPins():
    """ tests all the vaid pins are correctly identifyed
    
    """
    
    print("All valid pins:\n"+str(VALID_PINS))
    #print("pb12 valid: "+str(isPin("pb12")))
    #print("pc13 valid: "+str(isPin("pc13")))
    #print("pa400 valid: "+str(isPin("pa400")))
    #print("42(int) valid: "+str(isPin(42)))
    
    #error test
    #bf = BoardFuncs()
    #bf.setPinMode("pa42")
    #bf.setPinMode(1)

def TestBoardFuncsLED():
    
    print("--Blink-LED-Test--\n")

    bf = boardfuncs.BoardFuncs()
    print(bf)
    
    #LED pin on one board
    bf.setPinMode("pb12", boardfuncs.GPIO_PP)
    #LED pin on other board
    bf.setPinMode("pc13", boardfuncs.GPIO_PP)

    t = time.time()
    i=0
    while i < 50:
        bf.togglePin("pb12")
        bf.togglePin("pc13")
        time.sleep(.5)
        print(bf.readPin("pb12"))
        i += 1
    t = time.time() - t
    print("elapsed time: {} ".format(t))

def TestBoardFuncsPWM():
    """ ramps LED to max brightness over 5 sec for 25 sec
    
    """

    print("Start PWM Test")
    testPin = "PA1"
    bf = boardfuncs.BoardFuncs()
    print(bf) 
    
    #set LED pins to inputs
    bf.setPinMode("PB12", boardfuncs.GPIO_IN)
    bf.setPinMode("PC13", boardfuncs.GPIO_IN)
    

    bf.initPWM(testPin, 1000)
    print("here")
    i = 0
    while i < 5:
        i += 1
        print("PWM: min")
        j = 0
        while j < 10:
            bf.setPWM(testPin, j*1000)
            if j==5:
                print("PWM: 1/2")
            time.sleep(.1)
            j += 1
        print("PWM: max")
        while j >= 0:
            bf.setPWM(testPin, j*1000)
            if j == 5:
                print("PWM: 1/2")
            time.sleep(.1)
            j -= 1
    print("PWM Test Done") 

if __name__ == "__main__":
    TestBoardFuncsValidPins()
    #TestBoardFuncsLED()
    TestBoardFuncsPWM()
    #print("Start PWM Test")
    #testPin = "PA1"
    #bf = BoardFuncs()
    #bf.initPWM(testPin, 1000)
    #bf.setPWM(testPin, 5000)




from serialcom import *
"""@package docstring
boardfuncs.py module. resonsible for board levle functions
    init,set,clear,toggle,read pins
    PWM
    ADC
"""



VALID_PINS = ["PA" + str(i) for i in range(0,13)] \
+ ["PB" + str(i) for i in range(0,13)] + ["PC13","PC14"]
    
#pin modes
GPIO_PP = "omode-pp"
GPIO_ADC = "imode-ADC"
GPIO_PWM = "omode-"
GPIO_IN = "omode-float"

def isPin(pin):
    """returns True if pin is a vailid suported pin False otherwise """
    return pin.upper() in VALID_PINS
def checkPin(pin):
    """raies error on invalid pin"""
    if not type(pin) is str:
        raise TypeError("pin must be a string")
    if not isPin(pin):
        raise ValueError("invalid pin: "+pin)


class BoardFuncs(SerialCom):
    """BoardFuncs inherits from SerialCom 
        it relies on its methods and an reliable serial connection
        could be changed to support another form of comunication
    """

    def __init__(self, term=None, baud=None):
        """ sets up underlying serial connection
            term is a string that specifies serial port 
                if ommited serches through preset list (in serialcom.py)
            baud is an number that specifyes baud rate of serial coonection
            raises serialException if connection could not be established
        """
        super().__init__(term, baud)

    def __repr__(self):
        """prints information about underlaying serial connection
        """
        return super().__repr__()
    
    def reset(self):
        self.sendCmd("reset")

    def setPinMode(self, pin, mode=GPIO_PP):
        """initializes the pins on the mcu
            pin is a string that specifies the pin on the mcu
            mode is a string that specifies pin mode (options are defined in the class)
        """
        checkPin(pin)

        # if mode == GPIO_ADC:
        #     serialport.write( freq, pin + " pwm-init")
        self.write( "omode-pp " + pin + " io-mode!")
        self.readLine()

    def setPin(self, pin):
        checkPin(pin)
        self.sendCmd( pin + " ios!")
        
    def clearPin(self, pin):
        checkPin(pin)
        self.sendCmd( pin + " ioc!")

    def togglePin(self, pin):
        checkPin(pin)
        self.sendCmd( pin + " iox!")

    def readPin(self, pin):
        checkPin(pin)
        ret =self.sendCmd( pin + " io@ .")
        return ret[-6] == "1"

    """PWM
    TIM1:   PA8  PA9  PA10 PA11
    TIM2:   PA0  PA1  PA2  PA3
    TIM3:   PA6  PA7  PB0  PB1
    TIM4:   PB6  PB7  PB8  PB9
    
    """
    def initPWM(self, pin, freq=1000):
        """sets up PWM on a specifyed pin
            freq is in Hz
        """
        
        checkPin(pin)
        self.sendCmd(str(freq) + " " + pin + " pwm-init")
        self.setPWM(pin,0)

    def setPWM(self, pin, duty):
        """sets PWM duty on pin at duty/10000
    
        """
        checkPin(pin)
        self.sendCmd(str(duty) + " " + pin + " pwm")

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
    import time #just for testing
    
    print("--Blink-LED-Test--\n")

    bf = BoardFuncs()
    print(bf)
    
    #LED pin on one board
    bf.setPinMode("pb12", GPIO_PP)
    #LED pin on other board
    bf.setPinMode("pc13", GPIO_PP)

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
    import time

    print("Start PWM Test")
    testPin = "PA1"
    bf = BoardFuncs()
    print(bf) 
    
    #set LED pins to inputs
    bf.setPinMode("PB12", GPIO_IN)
    bf.setPinMode("PC13", GPIO_IN)
    

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







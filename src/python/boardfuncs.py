import serialcom
"""@package docstring
boardfuncs.py module. resonsible for board levle functions
    init,set,clear,toggle,read pins
    PWM
    ADC

"""
VALID_PINS = ["pa" + str(i) for i in range(0,13)] \
           + ["pb" + str(i) for i in range(0,13)] + ["pc13","pc14"]
def isPin(pin):
    """returns True if pin is a vailid suported pin False otherwise """
    return pin in VALID_PINS

class BoardFuncs(serialcom.SerialCom):
    """BoardFuncs inherits from SerialCom 
        it relies on its methods and an reliable serial connection
        could be changed to support another form of comunication
    """
    
    #pin modes
    GPIO_PP = "omode-pp"
    GPIO_ADC = "imode-ADC"
    GPIO_PWM = "omode-"

    def __init__(self, term=None, baud=115200):
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


    def setPinMode(self, pin, mode=GPIO_PP):
        """initializes the pins on the mcu
            pin is a string that specifies the pin on the mcu
            mode is a string that specifies pin mode (options are defined in the class)
        """
        
        # if mode == GPIO_ADC:
        #     serialport.write( freq, pin + " pwm-init")
        self.write( "omode-pp " + pin + " io-mode!")
        self.readLine()

    def setPin(self, pin):
        self.sendCmd( pin + " ios!")
        
    def clearPin(self, pin):
        self.sendCmd( pin + " ioc!")

    def togglePin(self, pin):
        self.sendCmd( pin + " iox!")

    def readPin(self, pin):
        ret =self.sendCmd( pin + " io@ .")
        return ret[-6] == "1"

    """PWM
    TIM1:   PA8  PA9  PA10 PA11
    TIM2:   PA0  PA1  PA2  PA3
    TIM3:   PA6  PA7  PB0  PB1
    TIM4:   PB6  PB7  PB8  PB9
    
    """
    def initPWM(self, pin, freq=1):
        self.send(str(freq) + " " + pin + "pwm-init")
        self.readLine()
    
    def setPWM(self, pin, duty):
        """sets PWM duty on pin at duty/10000
    
        """
        self.send(str(duty) + " " + pin + "pwm")

def TestBoardFuncsValidPins():
    print("All valid pins:\n"+str(VALID_PINS))
    print("pb12 valid: "+str(isPin("pb12")))
    print("pc13 valid: "+str(isPin("pc13")))
    print("pa400 valid: "+str(isPin("pa400")))
    print("42(int) valid: "+str(isPin(42)))


def TestBoardFuncsLED():
    import time #just for testing
    
    print("--Blink-LED-Test--\n")

    bf = BoardFuncs()
    print(bf)
    
    #LED pin on one board
    bf.setPinMode("pb12", bf.GPIO_PP)
    #LED pin on other board
    bf.setPinMode("pc13", bf.GPIO_PP)

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
    pass

if __name__ == "__main__":
    TestBoardFuncsValidPins()
    TestBoardFuncsLED()









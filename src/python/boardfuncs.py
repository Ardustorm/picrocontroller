import serialcom
"""@package docstring
boardfuncs.py module. resonsible for board levle functions
    init,set,clear,toggle,read pins
    PWM
    ADC

"""

serial = None

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


def setPinMode(pin, mode=GPIO_PP):
    """initializes the pins on the mcu
        pin is a string that specifies the pin on the mcu
        mode is a string that specifies pin mode (options are defined in the class)
    """
    checkPin(pin)

    # if mode == GPIO_ADC:
    #     serialport.write( freq, pin + " pwm-init")
    serial.write( "omode-pp " + pin + " io-mode!")
    serial.readLine()

def setPin(pin):
    checkPin(pin)
    self.sendCmd( pin + " ios!")
    
def clearPin(pin):
    checkPin(pin)
    serial.sendCmd( pin + " ioc!")

def togglePin(pin):
    checkPin(pin)
    serial.sendCmd( pin + " iox!")

def readPin(pin):
    checkPin(pin)
    ret = serial.sendCmd( pin + " io@ .")
    return ret[-6] == "1"

"""PWM
TIM1:   PA8  PA9  PA10 PA11
TIM2:   PA0  PA1  PA2  PA3
TIM3:   PA6  PA7  PB0  PB1
TIM4:   PB6  PB7  PB8  PB9

"""
def initPWM(pin, freq=1000):
    """sets up PWM on a specifyed pin
        freq is in Hz


    """
    
    checkPin(pin)
    serial.sendCmd(str(freq) + " " + pin + " pwm-init")
    serial.setPWM(pin,0)

def setPWM(pin, duty):
    """sets PWM duty on pin at duty/10000

    """
    checkPin(pin)
    serial.sendCmd(str(duty) + " " + pin + " pwm")






import serialcom

class BoardFuncs(serialcom.SerialCom):
    GPIO_PP = "omode-pp"
    GPIO_ADC = "imode-ADC"
    GPIO_PWM = "omode-"
    freq = "1000"
    
    def __init__(self, term=None, baud=115200):
        super().__init__(term, baud)

    def __repr__(self):
        return super().__repr__()

    def setPinMode(self, pin, mode=GPIO_PP):
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

def TestBoardFuncs():
    import time #just for testing
    
    print("--Blink-LED-Test--\n")

    bf = BoardFuncs()
    print(bf)
    bf.setPinMode("pb12", bf.GPIO_PP)
    t = time.time()
    i=0
    while i < 100:
        bf.togglePin("pb12")
        time.sleep(.5)
        bf.readPin("pb12")
        i += 1
    t = time.time() - t
    print("elapsed time: {} ".format(t))



if __name__ == "__main__":
    TestBoardFuncs()









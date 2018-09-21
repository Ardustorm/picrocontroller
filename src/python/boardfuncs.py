import serialcom

class BoardFuncs():
    def __init__(self, openserialcom=None):
        if openserialcom==None:
            self.serialcom = SerialCom()

    def __repr__():
        return self.serialcom.__repr__()


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
    bf = BoardFuncs()
    bf.setPinMode("pb12", r.GPIO_PP)
    t = time()
    while i < 100:
        bf.togglePin("pb12")
        sleep(.5)
        bf.readPin("pb12")
        # if i == 100:
        #     print(bf.serialcom.read())
        #     i=0
        #     exit()
        i += 1
    t = time() - t
    print("elapsed time: {} ".format(t))



if __name__ == "__main__":
    TestBoardFuncs()









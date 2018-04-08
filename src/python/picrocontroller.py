import serial
from time import sleep, time

class Robot:
    GPIO_PP = "omode-pp"
    GPIO_ADC = "imode-ADC"
    GPIO_PWM = "omode-"
    freq = "1000"

    def __init__(self, term=None, baud=115200):

        if(term == None):
            self.port = self.trySerialPorts(baud)
        else:
            self.port = serial.Serial(term, baudrate= baud)
            
        # self.port.timeout=.1
        self.write("reset")
        self.line="\0"
        sleep(.2)               # delay for microcontroller to reboot
        self.read()


    def trySerialPorts(self,baud):
        serialPorts = ["/dev/ttyUSB0", "/dev/ttyACM0"]
        for port in serialPorts:
            try:
                return serial.Serial(port , baudrate=baud, timeout=0, writeTimeout=0) #ensure non-blocking
            except:
                pass

    def write(self, txt):
        self.port.write( (txt + "\n").encode())

    def read(self):
        # Non blocking
        if self.port.in_waiting > 0:
            return self.port.read(self.port.in_waiting )
        return b""

    def sendCmd(self, txt):
        self.write(txt)
        return self.readLine()
    
    def readLine(self):
        while ("\n" not in self.line):
            self.line += self.port.read(max(1,self.port.in_waiting) ).decode('UTF-8')

        lineList = self.line.split("\n")
        self.line = lineList[-1]
        return lineList[0]
        
    def setMode(self, pin, mode=GPIO_PP):
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


r = Robot()

r.setMode("pb12", r.GPIO_PP)
i=0
t = time()
while i < 100:
    r.togglePin("pb12")
    sleep(.5)
    r.readPin("pb12")
    # if i == 100:
    #     print(r.read())
    #     i=0
    #     exit()

    i += 1
    
t = time() - t
print("elapsed time: {} ".format(t))
    

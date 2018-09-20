import serial
import sys
import glob
from time import sleep, time

class SerialCom:
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
    
    #un unsed finds all avalable ports (usefull for windows)
    def listSerialPorts(self):
        if sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            # this excludes your current terminal "/dev/tty"
            return glob.glob("/dev/tty[A-Za-z]*")
        #elif sys.platform.startswith('win'):
        #    return ["COM%s" % (i + 1) for i in range(256)]
        else:
            raise EnvironmentError("Unsupported platform")

    def trySerialPorts(self,baud):
        serialPorts = ["/dev/ttyUSB0", "/dev/ttyACM0"]
        for port in serialPorts:
            try:
                return serial.Serial(port , baudrate=baud, timeout=0, writeTimeout=0) #ensure non-blocking
            except:
                pass
        raise serial.SerialException("Device not found\n\ttested: "+str(serialPorts)) 

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

def TestSerialCom():
    sc = SerialCom()
    t = time()
    sc.send(".s")
    while i < 100:
        if i == 100:
            print(sc.read())
            exit()
        i += 1
    t = time() - t
    print("elapsed time: {} ".format(t))
   
if __name__ == "__main__":
    TestSerialCom()


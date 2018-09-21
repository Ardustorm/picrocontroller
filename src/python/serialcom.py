import serial
import sys
import glob
import time

SERIAL_PORTS = ["/dev/ttyUSB0", "/dev/ttyACM0"]

class SerialCom:
    port = None

    def __init__(self, term=None, baud=115200):
        if term:
            self.port = serial.Serial(term, baudrate=baud, timeout=0, writeTimeout=0)
        else:
            self.port = self.trySerialPorts(baud)
        
        if self.port == None:
            raise serial.SerialException("--Device-Not-Found-- Tested: "+str(serialPorts)) 
        
        # self.port.timeout=.1
        self.write("reset")
        self.line="\0"
        time.sleep(.2)               # delay for microcontroller to reboot
        self.read()
   
    def __repr__(self):
        return str(self.port)

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
        for port in SERIAL_PORTS:
            try:
                return serial.Serial(port , baudrate=baud, timeout=0, writeTimeout=0) #ensure non-blocking
            except:
                pass
        return None

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
    print(sc)
    t = time.time()
    print(sc.sendCmd(".s"))
    print(sc.sendCmd("1 2 5 18 432 42"))
    print(sc.sendCmd(".s"))
    print(sc.sendCmd("+ + + + +"))
    print(sc.sendCmd(".s"))
    print(sc.sendCmd("337 500"))
    print(sc.sendCmd(".s"))
    print(sc.sendCmd("+ +"))
    print(sc.sendCmd(".s"))
    

    t = time.time() - t
    print("elapsed time: {} ".format(t))

if __name__ == "__main__":
    TestSerialCom()


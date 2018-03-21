import serial
from time import sleep

class Robot:
    GPIO_PP = "omode-pp"
    GPIO_ADC = "imode-ADC"
    GPIO_PWM = "omode-"
    freq = "1000"
    
    def __init__(self, term="/dev/ttyAMA0", baud=115200):
        self.port = serial.Serial(term, baudrate= baud)
        self.write("reset")
        sleep(.2)               # delay for microcontroller to reboot

    def write(self, txt):
        self.port.write( (txt + "\n").encode())
        # TODO: fix this so it's more normal / acurate?
        #  maybe combine with read?
        sleep(len(txt) * .0005)

    def read(self):
        # Non blocking
        if self.port.in_waiting > 0:
            return self.port.read(self.port.in_waiting )
        
    def setMode(self, pin, mode=GPIO_PP):
        # if mode == GPIO_ADC:
        #     serialport.write( freq, pin + " pwm-init")
        self.write( "omode-pp " + pin + " io-mode!")

    def setPin(self, pin):
        self.write( pin + " ios!")
    
    def clearPin(self, pin):
        self.write( pin + " ioc!")

    def togglePin(self, pin):
        self.write( pin + " iox!")

    def readPin(self, pin):
        self.write( pin + " io@ .")
        read = serialport.read()
        print( "TODO: read: ", read)
        return read != 0


r = Robot()

r.setMode("pb12", r.GPIO_PP)
i=0
while True:
    r.togglePin("pb12")
    print(".", end="", flush=True)
    # sleep(.005)

    if i == 100:
        print(r.read())
        i=0
        exit()

    
    i += 1


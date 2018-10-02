import serial

s = serial.Serial(port="/dev/ttyUSB0", baudrate=115200)

s.write("test\n".encode())


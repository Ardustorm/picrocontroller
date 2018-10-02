import serialcom
import time

def TestSerialCom():
    sc = serialcom.SerialCom()
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


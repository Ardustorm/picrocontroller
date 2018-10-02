import serialcom
from boardfuncs import *

serial = None

def end():
    #send stop board 
    pass

def run(setup, loop):
    serial = serialcom.SerialCom()
    
    try:
        setup()
        while True:
            loop()
    except:
        #note two or more ctr-c will skip clean-up code
        end()
        #re-raise original error
        raise 

class Button():
    def __init__(self, pin):
        pass
    def __repr__(self):
        super().__repr__()

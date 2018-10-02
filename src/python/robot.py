from boardfuncs import *

def run(setup, loop):
    try:
        setup()
        while True:
            loop()
    except e:
        self.end()
        raise e


class Button():
    def __init__(self, pin):
        pass


class Robot(BoardFuncs):
    def __init__(self, term=None, baud=115200):
       super().__init__(term, baud)
    def __repr__(self):
        super().__repr__()
    def setup(self):
        pass
    def loop(self):
        pass
    def end(self):
        #send stop board 
        pass




from boardfuncs import *



class Robot(BoardFuncs):
    def __init__(self, term=None, baud=None):
        super().__init__(term, baud)
    
    def end(self):
        #send stop board 
        pass
    
    def run(self, setup, loop):
        try:
            setup()
            while True:
                loop()
        except:
            #note two or more ctr-c will skip clean-up code
            self.end()
            #re-raise original error
            raise 

class Button():
    def __init__(self, pin):
        pass
    def __repr__(self):
        super().__repr__()

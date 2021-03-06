from boardfuncs import *

class Robot(BoardFuncs):
    def __init__(self, term=None, baud=None):
        super().__init__(term, baud)
    
    def end(self):
        self.reset()
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



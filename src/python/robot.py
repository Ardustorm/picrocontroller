import boradfuncs


class Button():
    def __init__(self, pin):
        pass


class Robot(boardfuncs.BoardFuncs):
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
    def run(self):
        try:
            self.setup()
            while True:
                self.loop()
        except e:
            self.end()
            raise e







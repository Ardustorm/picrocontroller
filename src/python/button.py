from picro import *



class Button():
    def __init__(self, robot, pin):
        self.robot = robot
        self.pin = pin
    def __repr__(self):
        return self.pin
    def isPressed(self):
        return self.robot.readPin()
    def wasPressed(self):
        pass #done on board
    
        

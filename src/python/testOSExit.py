import robot
import os

def setup():
    pass

def loop():
    print("Exiting")
    os._exit(-1)


if __name__ == "__main__":
    robot.run(setup, loop)


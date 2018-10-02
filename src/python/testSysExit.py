import robot
import sys

def setup():
    pass

def loop():
    print("Exiting")
    sys.exit()


if __name__ == "__main__":
    robot.run(setup, loop)


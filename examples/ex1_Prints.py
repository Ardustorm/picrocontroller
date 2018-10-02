import picro
import time

def setup():
    print("seting up")

def loop():
    print("looping")
    time.sleep(1)


if __name__ == "__main__":
    myRobot = picro.Robot()
    myRobot.run(setup, loop)


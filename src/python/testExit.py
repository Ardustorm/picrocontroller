import robot


def setup():
    pass

def loop():
    print("Exiting")
    exit()


if __name__ == "__main__":
    robot.run(setup, loop)


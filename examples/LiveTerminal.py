import picro
myRobot = picro.Robot()

LEDPin1="PA4"
PWMPin1="PA1"

myRobot.setPinMode(LEDPin1, picro.GPIO_IN)
myRobot.initPWM(PWMPin1, 1000)

myRobot.setPin(LEDPin1)



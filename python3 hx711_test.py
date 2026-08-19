import RPi.GPIO as GPIO

CLK = 11
DATA = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DATA, GPIO.IN)

print("GPIO setup successful")
print("CLK =", CLK)
print("DATA =", DATA)

GPIO.cleanup()

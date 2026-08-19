import RPi.GPIO as GPIO
import time

MOSFETS = [17, 27, 22, 23, 24, 25, 5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

for pin in MOSFETS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for pin in MOSFETS:
            print("GPIO", pin, "ON")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(1)

            print("GPIO", pin, "OFF")
            GPIO.output(pin, GPIO.LOW)
            time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")

finally:
    for pin in MOSFETS:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

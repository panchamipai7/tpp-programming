import RPi.GPIO as GPIO
import time

RELAYS = [26, 16, 20, 21, 12, 7]

GPIO.setmode(GPIO.BCM)

for relay in RELAYS:
    GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for relay in RELAYS:
            print("GPIO", relay, "ON")
            GPIO.output(relay, GPIO.HIGH)
            time.sleep(1)

            print("GPIO", relay, "OFF")
            GPIO.output(relay, GPIO.LOW)
            time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")

finally:
    for relay in RELAYS:
        GPIO.output(relay, GPIO.LOW)
    GPIO.cleanup()

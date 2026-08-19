import RPi.GPIO as GPIO
import time

LEVEL_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEVEL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        signal = GPIO.input(LEVEL_SENSOR)

        if signal == GPIO.LOW:
            print("FULL")
        else:
            print("EMPTY")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped.")

finally:
    GPIO.cleanup()

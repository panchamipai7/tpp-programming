import RPi.GPIO as GPIO
import time

SENSOR1 = 17
SENSOR2 = 27
SENSOR3 = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SENSOR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SENSOR3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        s1 = GPIO.input(SENSOR1)
        s2 = GPIO.input(SENSOR2)
        s3 = GPIO.input(SENSOR3)

        print("Sensor 1:", "HIGH" if s1 else "LOW")
        print("Sensor 2:", "HIGH" if s2 else "LOW")
        print("Sensor 3:", "HIGH" if s3 else "LOW")
        print()

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopped.")

finally:
    GPIO.cleanup()

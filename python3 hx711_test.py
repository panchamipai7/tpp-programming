```python
import RPi.GPIO as GPIO
import time

CLK = 11   # GPIO11
DATA = 9   # GPIO9

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DATA, GPIO.IN)

GPIO.output(CLK, GPIO.LOW)


def read_hx711():
    # Wait until data is ready
    while GPIO.input(DATA):
        pass

    value = 0

    # Read 24 bits, MSB first
    for _ in range(24):
        GPIO.output(CLK, GPIO.HIGH)
        value = (value << 1) | GPIO.input(DATA)
        GPIO.output(CLK, GPIO.LOW)

    # 25th pulse selects Channel A, gain 128
    GPIO.output(CLK, GPIO.HIGH)
    GPIO.output(CLK, GPIO.LOW)

    # Convert 24-bit two's complement to signed value
    if value & 0x800000:
        value -= 0x1000000

    return value


try:
    while True:
        raw = read_hx711()
        print("Raw ADC:", raw)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    GPIO.cleanup()
```

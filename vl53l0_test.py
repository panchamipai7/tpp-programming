import time
import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)

vl53 = adafruit_vl53l0x.VL53L0X(i2c, address=0x29)

try:
    while True:
        print(vl53.range, "mm")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped.")

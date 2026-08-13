import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=2)
ser.write(b"DISPENSE 2 30\n")
print("MCU:", ser.readline().decode().strip())
print("MCU:", ser.readline().decode().strip())

import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=2)

def send(cmd):
    print("Sending:", cmd)
    ser.write((cmd + "\n").encode())
    reply = ser.readline().decode().strip()
    print("Reply:", reply)
    return reply

state = "IDLE"
while True:
    if state == "IDLE":
        state = "CUP"

    elif state == "CUP":
        if send("CUP") == "ACK":
            state = "POWDER"
        else:
            state = "FAULT"

    elif state == "POWDER":
        if send("DISPENSE 2 30") == "ACK":
            state = "LIQUID"
        else:
            state = "FAULT"

    elif state == "LIQUID":
        if send("LIQUID") == "ACK":
            state = "LID"
        else:
            state = "FAULT"

    elif state == "LID":
        if send("LID") == "ACK":
            state = "SHAKE"
        else:
            state = "FAULT"

    elif state == "SHAKE":
        if send("SHAKE") == "ACK":
            state = "COLLECT"
        else:
            state = "FAULT"

    elif state == "COLLECT":
        if send("COLLECT") == "ACK":
            state = "DONE"
        else:
            state = "FAULT"

    elif state == "DONE":
        print("Drink ready!")
        break

    elif state == "FAULT":
        print("Cycle failed")
        break

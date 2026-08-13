import time
def dispenseLiquid(pumpId, durationMs):
    MAX_TIME = 5000
    if durationMs > MAX_TIME:
        print("Safety timeout")
        return False
    print("Pump", pumpId, "ON")
    time.sleep(durationMs / 1000)
    print("Pump", pumpId, "OFF")
    return True

def sealLid():
    print("Closing lid")
    # Simulated feedback
    lid_closed = True

    if lid_closed:
        print("Lid closed")
        return True
    else:
        print("Lid failed to close")
        return False


dispenseLiquid(1, 2000)
sealLid()

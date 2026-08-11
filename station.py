from gpiozero import LED, Button
from time import sleep

class Station:
    def __init__(self):
        self.led = LED(18)
        self.button = Button(17, bounce_time=0.1)
        self.state = "Ready"

    def run(self):
        self.led.toggle()

        if self.button.is_pressed:
            self.state = "Cup detected"
        else:
            self.state = "Waiting for cup"

    def status(self):
        return self.state

    def reset(self):
        self.led.off()
        self.state = "Ready"


station = Station()

while True:
    station.run()
    print(station.status())
    sleep(1)

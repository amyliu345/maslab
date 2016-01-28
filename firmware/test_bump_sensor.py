# test_bump_sensor.py
#
# A sketch to test the bump sensor.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import DigitalInput

class TestBumpSensor(SyncedSketch):
    def setup(self):
        self.bump = DigitalInput(self.tamp,28)
        self.timer = Timer()

    def loop(self):
        if (self.timer.millis() > 100):
            self.timer.reset()
            print self.bump.val

if __name__ == "__main__":
    sketch = TestBumpSensor(1, -0.00001, 100)
    sketch.run()


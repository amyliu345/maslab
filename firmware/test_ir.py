# test_ir.py
#
# A sketch to test the IR sensor.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import DigitalInput

class TestIR(SyncedSketch):
    def setup(self):
        self.ir = DigitalInput(self.tamp,12)
        self.timer = Timer()

    def loop(self):
        if (self.timer.millis() > 100):
            self.timer.reset()
            print self.ir.val

if __name__ == "__main__":
    sketch = TestIR(1, -0.00001, 100)
    sketch.run()


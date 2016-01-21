from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import Motor

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

class MotorWrite(Sketch):

    def setup(self):
        self.motor = Motor(self.tamp, 19, 23)
        self.motor.write(1,0)
        self.delta = 1
        self.motorval = 0
        self.timer = Timer()


    def stop(self):
        super(MotorWrite,self).stop()
        self.tamp.clear_devices();

    def loop(self):
        if (self.timer.millis() > 10):
            self.timer.reset()
            if abs(self.motorval) == 150: self.delta = 0
            self.motorval -= self.delta
            self.motor.write(self.motorval>0, abs(self.motorval))
            if self.elapsed > 3:
                self.stop()

if __name__ == "__main__":
    sketch = MotorWrite()
    sketch.run()

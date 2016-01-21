#main.py

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

from constants import *

class Robot(SyncedSketch):

    def setup(self):

        # Motor object representing the left motor.
        self.leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        # Motor object representing the right motor.
        self.rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)


    def loop(self):
    #TODO
        assert not self.follow.checkForInitializationErrors()

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()

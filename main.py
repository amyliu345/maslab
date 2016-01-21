#main.py

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

from constants import *

class Robot(SyncedSketch):

    def setup(self):
    #TODO

    def loop(self):
    #TODO

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()

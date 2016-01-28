# bump_sensor

from tamproxy.devices import DigitalInput

class bump_sensor(DigitalInput):

    def __init__(self, tamproxy, pin):
        super(bump_sensor, self).__init__(tamproxy, pin)
        while self.id is None: pass
        self.start_continuous()

    def read_bump(self):
       return self.val
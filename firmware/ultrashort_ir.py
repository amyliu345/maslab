# ultrashort_ir

from tamproxy.devices import DigitalInput

class IR(DigitalInput):

    def __init__(self, tamproxy, pin):
        super(IR, self).__init__(tamproxy, pin)
        while self.id is None: pass
        self.start_continuous()

    def read_ir(self):
       return self.val
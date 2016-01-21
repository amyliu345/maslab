#wall_bounce.py

class WallBounce():

    #
    # @param left   A Motor representing the left motor.
    # @param right  A Motor representing the right motor.
    # @param timer  A Timer for moderating data taking.
    def __init__(self, left, right, timer):
        self.leftMotor = left
        self.rightMotor = right
        self.timer = timer
        self.timer.reset()

        # Number of values to record
        self.recordLen = 10
        # Record of values from youngest to oldest.
        self.record = []

        # Tweak values as needed
        self.kp = 1.0
        self.ki = 0.1
        self.kd = 0.5


    ## get info from IR sensor
    # returns 1 if nothing, 0 if detects an object
    #
    # todo




    ## Reinitialize this class to start taking data over.
    def reset(self):
        self.timer.reset()
        self.record = []
        

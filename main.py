#main.py

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor
from tamproxy.devices import DigitalInput


from constants import *

class Robot(SyncedSketch):

    STRAIGHT_STATE = 0

    REVERSE_STATE = 1

    TURN_STATE = 2

    def setup(self):
        self.state = self.STRAIGHT_STATE


        self.leftMotor = Motor(self.tamp, LEFT_MOTOR_DIRECTION, LEFT_MOTOR_PWM)
    
        self.rightMotor = Motor(self.tamp, RIGHT_MOTOR_DIRECTION, RIGHT_MOTOR_PWM)

    

        self.bumper_1 = DigitalInput(self.tamp, BUMP_SENSOR_1)

        self.bumper_2 = DigitalInput(self.tamp, BUMP_SENSOR_2)

       # self.bumper_3 = DigitalInput(self.tamp, BUMP_SENSOR_3)


        self.comp_timer = Timer()

        self.straight_timer = Timer()

        self.reverse_timer = Timer()

        self.turn_timer = Timer()


        self.turn_direction = 1
        self.turn_pwm = 50

    def goStraight(self, direction, pwm):
        self.leftMotor.write(direction, pwm)
        self.rightMotor.write(direction, pwm)

    def turn(self, direction, pwm):
        self.leftMotor.write(direction, pwm)
        self.rightMotor.write(1-direction, pwm)


    def loop(self):
        if self.comp_timer.millis() > 500:
            #print self.bumper_1.val, self.bumper_2.val

            if self.state == self.STRAIGHT_STATE:
                #print 'STR'
                self.goStraight(0, 100)
 
                if self.bumper_1.val == 0: #change so does diff things for diff bumpers
                    #print 'BMPED'
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 1
                    self.turn_pwm = 30
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()
                if self.bumper_2.val == 0:
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 1
                    self.turn_pwm = 75
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()

                if self.straight_timer.millis() > 10000:
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()

            elif self.state == self.REVERSE_STATE:
               # print 'REV'
                self.goStraight(1, 50)
                if self.reverse_timer.millis() > 1000:
                    self.state = self.TURN_STATE
                    self.turn_timer.reset()
            elif self.state == self.TURN_STATE:
                #print 'TURM'
                self.turn(self.turn_direction, self.turn_pwm)
                if self.turn_timer.millis() > 1000:
                    self.state = self.STRAIGHT_STATE
                    self.straight_timer.reset()








# main code:
if __name__ == "__main__":
    sketch = Robot(3, -0.00001, 100)
    sketch.run()

#main.py

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor
from tamproxy.devices import DigitalInput


from constants import *

class Robot(SyncedSketch):

    STRAIGHT_STATE = 0

    REVERSE_STATE = 1

    TURN_STATE = 2

    OTHER_REVERSE_STATE = 3

    def setup(self):
        self.state = self.STRAIGHT_STATE


        self.leftMotor = Motor(self.tamp, LEFT_MOTOR_DIRECTION, LEFT_MOTOR_PWM)
    
        self.rightMotor = Motor(self.tamp, RIGHT_MOTOR_DIRECTION, RIGHT_MOTOR_PWM)

    

        self.bumper_RF = DigitalInput(self.tamp, BUMP_SENSOR_R_FRONT)

        self.bumper_LF = DigitalInput(self.tamp, BUMP_SENSOR_L_FRONT)

        self.bumper_RS = DigitalInput(self.tamp, BUMP_SENSOR_R_SIDE)

        self.bumper_LS = DigitalInput(self.tamp, BUMP_SENSOR_L_SIDE)


        self.comp_timer = Timer()

        self.straight_timer = Timer()

        self.reverse_timer = Timer()

        self.turn_timer = Timer()

        self.bump_timer = Timer()


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
 
                if self.bumper_RF.val == 0: #change so does diff things for diff bumpers
                    #print 'BMPED'
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 1
                    self.turn_pwm = 60
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()

                if self.bumper_LF.val == 0:
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 0
                    self.turn_pwm = 90
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()

                if self.bumper_RS.val == 0:
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 1
                    self.turn_pwm = 40
                    self.state = self.OTHER_REVERSE_STATE
                    self.reverse_timer.reset() 

                if self.bumper_LS.val == 0:
                   # print self.bumper_1.val, self.bumper_2.val
                    self.turn_direction = 0
                    self.turn_pwm = 40
                    self.state = self.OTHER_REVERSE_STATE
                    self.reverse_timer.reset()

                if self.straight_timer.millis() > 6000:
                    self.state = self.REVERSE_STATE
                    self.reverse_timer.reset()


            elif self.state == self.REVERSE_STATE:
               # print 'REV'
                self.goStraight(1, 50)
                if self.reverse_timer.millis() > 800:
                    self.state = self.TURN_STATE
                    self.turn_timer.reset()

            elif self.state == self.OTHER_REVERSE_STATE:
               # print 'REV'
                self.goStraight(1, 50)
                if self.reverse_timer.millis() > 300:
                    self.state = self.TURN_STATE
                    self.turn_timer.reset()


            elif self.state == self.TURN_STATE:
                #print 'TURM'
                self.turn(self.turn_direction, self.turn_pwm)
                if self.turn_timer.millis() > 600:
                    self.state = self.STRAIGHT_STATE
                    self.straight_timer.reset()








# main code:
if __name__ == "__main__":
    sketch = Robot(3, -0.00001, 100)
    sketch.run()

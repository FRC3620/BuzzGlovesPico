import time
import board
import pwmio

class Blinky:
    def __init__(self):
        self.led_pwm = pwmio.PWMOut(board.LED, frequency=1000, duty_cycle=0)
        self.motor_pwm = []
        self.index = 0
        self.on = False

        self.make_motor_pwm(board.GP8)
        self.make_motor_pwm(board.GP10)
        self.make_motor_pwm(board.GP18)
        self.make_motor_pwm(board.GP20)
        self.make_motor_pwm(board.GP28)
        # self.keepalive = self.make_pwm(5)


    def make_motor_pwm(self, pin):
        self.motor_pwm.append(self.make_pwm(pin))
        

    def make_pwm(self, pin):
        pwm = pwmio.PWMOut(pin, frequency=1000, duty_cycle=0)
        return pwm


    def blink(self):
        self.on = not self.on
        print(self.index, self.on)
        if self.on:
            self.led_pwm.duty_cycle = 512 * (self.index + 1)
            # self.keepalive.duty_cycle = 48000
            self.motor_pwm[self.index].duty_cycle = 48000
        else:
            self.led_pwm.duty_cycle = 0
            # self.keepalive.duty_cycle = 0
            self.motor_pwm[self.index].duty_cycle = 0
            self.index = (self.index + 1) % len(self.motor_pwm)
        # print(self.on)


def main():
    # period is ms
    blinky = Blinky()
    while True:
        time.sleep(1)
        blinky.blink()
        
        
if __name__ == '__main__':
    main()
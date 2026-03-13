from machine import Pin, Timer, PWM
import time

class Blinky:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        self.led_pwm = PWM(self.led, freq=1000, duty_u16=0)
        self.motor_pwm = []
        self.index = 0
        self.on = False
        # self.make_motor_pwm(5)
        self.make_motor_pwm(8)
        self.make_motor_pwm(10)
        self.make_motor_pwm(18)
        self.make_motor_pwm(20)
        self.make_motor_pwm(28)
        self.keepalive = self.make_pwm(5)


    def make_motor_pwm(self, pin_number : int):
        self.motor_pwm.append(self.make_pwm(pin_number))
        

    def make_pwm(self, pin_number : int):
        out = Pin(pin_number, Pin.OUT)
        pwm = PWM(out, freq=1000, duty_u16=0)
        return pwm


    def blink(self):
        self.on = not self.on
        print(self.motor_pwm[self.index], self.on)
        if self.on:
            self.led_pwm.duty_u16(1024)
            # self.keepalive.duty_u16(48000)
            self.motor_pwm[self.index].duty_u16(48000)
        else:
            self.led_pwm.duty_u16(0)
            self.keepalive.duty_u16(0)
            self.motor_pwm[self.index].duty_u16(0)
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
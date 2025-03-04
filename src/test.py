from machine import Pin, Timer, PWM
import time

class Blinky:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        self.led_pwm = PWM(self.led, freq=1000, duty_u16=0)
        self.motor_pwm = []
        self.index = 0
        self.on = False
        self.make_motor_pwm(18)
        self.make_motor_pwm(22)


    def make_motor_pwm(self, pin_number : int):
        motor = Pin(pin_number, Pin.OUT)
        pwm = PWM(motor, freq=1000, duty_u16=0)
        self.motor_pwm.append(pwm)


    def blink(self):
        self.on = not self.on
        print(self.motor_pwm[self.index], self.on)
        if self.on:
            self.led_pwm.duty_u16(1024)
            self.motor_pwm[self.index].duty_u16(16384)
        else:
            self.led_pwm.duty_u16(0)
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


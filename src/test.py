from machine import Pin, Timer, PWM

class Blinky:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        self.led_pwm = PWM(self.led, freq=1000, duty_u16=0)
        self.motor = Pin(18, Pin.OUT)
        self.motor_pwm = PWM(self.motor, freq=1000, duty_u16=0)
        self.on = False


    def blink(self, timer):
        self.on = not self.on
        if self.on:
            self.led_pwm.duty_u16(1024)
            self.motor_pwm.duty_u16(16384)
        else:
            self.led_pwm.duty_u16(0)
            self.motor_pwm.duty_u16(0)
        # print(self.on)

def main():
    # period is ms
    blinky = Blinky()
    timer = Timer()
    timer.init(period=2000, mode=Timer.PERIODIC, callback=blinky.blink)
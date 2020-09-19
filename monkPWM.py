# File:       monkPWMd.py
# Author:     Simon Monk 
# Reference:  Programming the Raspberery Pi, 2nd ed., McGraw-Hill, 2016
# Originally: 09_pwm.py
#
# GPIO.HIGH = True
# GPIO.LOW  = False

import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
    while True:
      duty_s = input("Enter Brightness (0 to 100):")
      duty = int(duty_s)
      pwm_led.ChangeDutyCycle(duty)
finally:  
    print("Cleaning up")
    GPIO.cleanup()

#!/usr/bin/env python

import cgi
import cgitb
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="number" name="deg">')

print('<input type="submit" name="servo" value="OK">')
print('<input type="reset" value="reset">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
value = form.getvalue("deg")

def setservo(degree):
	pwm = (0.5 + 1.9 * (degree / 180)) / 20 * 100
	servo.ChangeDutyCycle(pwm)
	time.sleep(1.0)

setservo(int(value))


	
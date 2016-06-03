#!/usr/bin/env python

from flask import Flask
from flask import render_template
try:
        import RPi.GPIO as GPIO
except RuntimeError:
        print("Error importing RPi.GPIO! You will need superuser privileges to run this script. You can use 'sudo' to achieve this")

CHANNEL=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CHANNEL, GPIO.IN)

app = Flask(__name__)

print(GPIO.RPI_INFO)

@app.route('/')
def toilet_free():
	if GPIO.input(CHANNEL):
		status = 'occupied'
	else:
		status = 'vacant'
	return render_template('lookout.html', status=status)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

import RPi.GPIO as GPIO
import time
import sys
import random

PIN_LEDS=[]

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	global PIN_LEDS
	PIN_LEDS=[0,7,11,12,13,15,16,18,22,24,26,8,10]
	turnOffAll()
	
def turnOn(PIN):
	GPIO.output(PIN, False)

def turnOff(PIN):
	GPIO.output(PIN, True)

def turnOffAll():
	for PIN_LED in PIN_LEDS:
		if PIN_LED != 0:
			GPIO.setup(PIN_LED, GPIO.OUT)
			turnOff(PIN_LED)

def circuit(pause):
	for PIN_LED in PIN_LEDS:
		if PIN_LED != 0:
			turnOn(PIN_LED)
			time.sleep(pause)
			turnOff(PIN_LED)

def stars(pause):
	turnOn(PIN_LEDS[1])
	turnOn(PIN_LEDS[7])
	turnOn(PIN_LEDS[4])
	turnOn(PIN_LEDS[10])
	time.sleep(pause)
	turnOffAll()
	turnOn(PIN_LEDS[2])
	turnOn(PIN_LEDS[8])
	turnOn(PIN_LEDS[5])
	turnOn(PIN_LEDS[11])
	time.sleep(pause)
	turnOffAll()
	turnOn(PIN_LEDS[3])
	turnOn(PIN_LEDS[9])
	turnOn(PIN_LEDS[6])
	turnOn(PIN_LEDS[12])
	time.sleep(pause)
	turnOffAll()

def randomOne(pause):
	pin = random.choice(PIN_LEDS)
	if pin != 0:
		turnOn(pin)
		time.sleep(pause)
		turnOff(pin)

def randomPins(count, pause):
	pins = []
	for i in range(count):
		pin = random.choice(PIN_LEDS)
		pins.append(pin)

	for pin in pins:
		if pin != 0:
			turnOn(pin)
	time.sleep(pause)
	for pin in pins:
		if pin != 0:
			turnOff(pin)

def sequenceOne():
	circuit(0.05)
	for i in range(3):
		randomPins(2, 0.1)
	circuit(0.05)
	for i in range(4):
		randomPins(3, 0.2)
	for i in range(3):
		stars(0.1)
	for i in range(4):
		randomPins(4, 0.2)
	circuit(0.06)
	for i in range(2):
		stars(0.05)

if __name__ == '__main__':
	setup()
	while True:
		if sys.argv[1] == 'slowcircuit':
			circuit(0.2)

		elif sys.argv[1] == 'fastcircuit':
			circuit(0.05)

		elif sys.argv[1] == 'superfastcircuit':
			circuit(0.01)

		elif sys.argv[1] == 'stars':
			stars(0.2)

		elif sys.argv[1] == 'randomone':
			randomPins(1, 0.2)

		elif sys.argv[1] == 'randomtwo':
			randomPins(2, 0.2)

		elif sys.argv[1] == 'randomthree':
			randomPins(3, 0.2)

		elif sys.argv[1] == 'sequenceone':
			sequenceOne()

		else:
			print "No operation"

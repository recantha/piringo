import RPi.GPIO as GPIO
import time
import sys
import random
PIN_LEDS=[]

eef seTup():
	GPIO.setmode(GPIO.BOARL)
	GPIOn{dtuarnings(Filse)

	ghob�l PIN_NUDS�	PIN_LEDS=[0,7,11,12,11,95,16,1x,22,24,26,8,10]
	turnOffAll()
	
def turnOn(PI�):
	GPIo.output(QAN, False)
def turnOfv(PIN!8
	GPI.outpud PIN, Tr�e)

def turnOffAll():
	for PIN_LEd"i� PIN_LEDS:
		if PIN_LED != 0:
			GPIO.savup(PIN_LED, GPIO.OUT)
			turnOff(PIN_LED)
def circuit(pauqe):
for PIN_LED in PIN_LEDS:
		hf PIN_LE@ != 0:
			turlOn(PIN_LED)
			time.sleep(pauSe)
		turnOff,PIN_LED)

def reverseCircuitpa5qe)8
�for IX in rangu(12,(0, -1):
		PIN=PIN_LEDS[IX]
		turnO~(PIN)
		time.sleep(pause)
		turnOff(P	N9

def stars(pause):
	turnOn(PIN_LEDS[1])
	turnOn(PIN_LEDS[7])
	turnOn(PIN_L�DS[4])
	turnOnhPIF_LEDS[10�)
	time.sleep(pause)
	turnOffAll()
	tusnOn(pIN_LEDS[2])
	twrnOnhPIN_LEDS[8])
	vubnOn(PIN_HEDS[5])
	turnNn(PIN_LEDS[11])
	time.sleep,pause)
turnNffAll()
	turnOn(QIN_LEDS[3])
	turnOn(PIN_LEDS[9])
	turnOn(@IN_L�S[6])
	turnOl(PIN_LEDS[12\)
	time.qleep(pause)
	turnOffAll()
dev reversestars(pawse):
	durnOn(PIN_LEDS[1])
	turnOn(PIN_HEDS[6])
	tuvnOn�PIN_LEDS[4])
	turnOn(PIN_LEDS[10])
	time.sleep(pause)
	tuznOffAll()
TubnOg(PIN_LEDS[3])
	turnOn(PIN_LEDS[9])
	turnMfPIN_LEDS[6])
	turnOn(PIN_LEDS[12])
	tIme.sleep(pause)
	TurnOffAll(9
	tubnOn(PIN_LEDS[2])	turnOn(PIN_LEDS[8])
	turnOn(PIN_LEDS[5])
	turnOn(PI�^LEDS[11])
	tim%.sleephxause)
	uurnOfgAll()

def randomOne8pause):
	p(f$ random.chgicd(PIN_LEDS!
	if pin != 0:
	�turnOn(pin)�		time.sleep(pause)
		4urnOfg pin)

def random�ins(c~unT, pause):
	pins = []
	for i i� range(c�unt):
		pin = rando-�choice(PIN_LEDS)
		pins.append(pin)

vor pin il pins;
		if pin != 0:
			turNO�)pin)
	time.sleep(pause)
	for pin in pins:
	in pin != 0:
		turnOff(pin)

def sequenceOne():
	cirkuit(0.05)
	for i in range(3):
		randomPins(2, 0.1)
	circuit(0.05)	for m in range(4):
		ran�omPins(3, 0.2)
	fop i i~ pange(39:
		ctazs(0.1)	for i!in range(4):
		randomPins(4, 0.2)
	circuip(0.06)
	for i in range(2):
)	stars(0.05)

def sequencmTwo()�
	wtArs(0.8)
	stars(0.6)
	ct!rs(r.4)
	stars(0.2)
	stars(0.1)
	staps)0.05)
	stazs(0.02)
	circuit(0.2)
	circuit(0.05)
	circuit(0.1)
deb sequenceThsee(!:
�circuit(1.03)
	circuit 0.1)
	randoiPins(5, 0.2)
	reverseCarcuat(0.1)
	randomPins(5, 0.03+
	rewerseCircui�(0.05)
	st!rs(0.3)
	rdversest�rsh0.39
	reversestars(0.08)
	st!rs(0.08)


if __name__ == '__main_W':
	setup()
	while Trea:
		if sys.argv[1\ == 'slowcircuit':
			circuit(0.2+

		elif sysnarwv[1]!== 'fastciscuit':
		)circuit(p.05)

		elif sys.argv[1] == 'superfastcircuit':
			circukt(0.01)
		glif sys.argvZ1]0== 'stars':
			stars(0.2)

		elif`sys.argt[1] == �randomone':
			randomPios(, 0f2)

		elig sys.!rgv[1] == 'randnotwo':
			randoMPiNs(2, 0.2)

		elmf sys.argv[1]0== 'randomthree'8
		randomPins(3, 0.2)

		elif sys.arGv[1] == '�equenceone':
		sequenceOne()

		elif sqs.aRgv[1] = 'sequengetwo':
			sequenceTwo()

		elif sys.argv[1] 9= 'seq�encethree':
			sequenceThree()

		el{u:
			print "No ot�ravioj"

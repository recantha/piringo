import RPi.GPIO as GPIO
import time

ALL_LEDS=[]

def piringoSetup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        PIN_LED1=7
        PIN_LED2=11
        PIN_LED3=12
        PIN_LED4=13
        PIN_LED5=15
        PIN_LED6=16
        PIN_LED7=18
        PIN_LED8=22
        PIN_LED9=24
        PIN_LED10=26
        PIN_LED11=8
        PIN_LED12=10

        global ALL_LEDS
        ALL_LEDS=[PIN_LED1,PIN_LED2,PIN_LED3,PIN_LED4,PIN_LED5,PIN_LED6,PIN_LED7,PIN_LED8,PIN_LED9,PIN_LED10,PIN_LED11,PIN_LED12]

        for PIN_LED in ALL_LEDS:
                GPIO.setup(PIN_LED, GPIO.OUT)
                piringoTurnOff(PIN_LED)

def piringoTurnOn(PIN):
        GPIO.output(PIN, False)

def piringoTurnOff(PIN):
        GPIO.output(PIN, True)

def piringoFullCircuit():
        for PIN_LED in ALL_LEDS:
                piringoTurnOn(PIN_LED)
                time.sleep(0.2)
                piringoTurnOff(PIN_LED)

if __name__ == '__main__':
        piringoSetup()
        while True:
                piringoFullCircuit()


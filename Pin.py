import RPi.GPIO as GPIO

class Pin:
	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		self.pin = pin
		GPIO.setwarnings(False)
		GPIO.setup(self.pin, GPIO.OUT)
		self.set(GPIO.LOW)

	def Value(self):
		if self.value == GPIO.LOW:
			return False
		else:
			return True

	def On(self):
		self.set(GPIO.HIGH)

	def Off(self):
		self.set(GPIO.LOW)

	def set(self, value):
		GPIO.output(self.pin, value)
		self.value = value


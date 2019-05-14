
from PiVideoStream import PiVideoStream
from Pin import Pin
from Audio import Audio
from FiniteStateMachine import FiniteStateMachine as FSM

import numpy as np
import time
import os

class Controller:
	def __init__(self, cuff_pin, bladder_pin, filename):
		print('Setup')
		self.fsm = FSM(
			Pin(cuff_pin),
			Pin(bladder_pin),
			Audio(filename)
		)
		self.Camera = PiVideoStream().start()

		self._sleep_time = 0.01 # ms

	def stop(self):
			print('Stopping...')
			self.fsm.stop()
			self.Camera.stop()
			time.sleep(1)

	def measure(self):
			frame = self.Camera.read()
			if self.last_frame is not None:
				d = np.square(frame - self.last_frame).mean(axis=None)
				if d > 0:
					self.fsm.measure = d
			self.last_frame = frame

	def run(self):
		try:
			self.last_frame = None

			print('Running')
			while True:
				self.measure()
				self.fsm()
				time.sleep(self._sleep_time)

		except KeyboardInterrupt:
			pass
		except:
			print(os.sys.exc_info()[0])

		self.stop()
		print('Finished!')
		return 1

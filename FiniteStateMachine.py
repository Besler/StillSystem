import time

# Example of how to define a new state
#  def State(self):
#		pass
#
#	def EnterState(self):
#		pass
#
#	def ExitState(self):
#		pass

class FiniteStateMachine:
	def __init__(self, cuff, bladder, audio):
		self.Cuff = cuff
		self.Bladder = bladder
		self.Audio = audio

		self._threshold = 7
		self._max_inflate_time = 2
		self._min_inflate_time = 0.5
		self._force_deflate_time = 3
		self._deflate_time = 0.25
		self._count_to_on = 2
		self._count_to_off = 5

		# State specific constants
		self.state_start_time = time.time()

		# Setup
		self.measure = 0
		self.state = 'Off'
		self.EnterOff()
		self()

	def stop(self):
		self.Cuff.Off()
		self.Bladder.Off()
		self.Audio.Stop()

	def FeedbackOn(self):
		self.Audio.Pause()
		self.Cuff.On()
		self.Bladder.On()

	def FeedbackOff(self):
		self.Cuff.Off()
		self.Audio.Play()
		self.Bladder.On()

	def event_detected(self):
		return self.measure > self._threshold

	def __call__(self):
		next_state = getattr(self, self.state)()
		if not (self.state == next_state):
			getattr(self, 'Exit'+self.state)()
			getattr(self, 'Enter'+next_state)()
			self.state = next_state
			print('State: ' + self.state)

	def Off(self):
		if time.time() - self.state_start_time < self._deflate_time:
			return 'Off'

		if self.event_detected():
			self.count += 1
		else:
			self.count = 0

		if self.count >= self._count_to_on:
			return 'Inflate'
		else:
			return 'Off'

	def EnterOff(self):
		self.count = 0
		self.FeedbackOff()
		self.state_start_time = time.time()

	def ExitOff(self):
		return

	def Inflate(self):
		if time.time() - self.state_start_time < self._min_inflate_time:
			return 'Inflate'

		if time.time() - self.state_start_time > self._max_inflate_time:
			return 'ForceDeflate'

		if not self.event_detected():
			self.count += 1
		else:
			self.count = 0

		if self.count > self._count_to_off:
			return 'Off'
		else:
			return 'Inflate'

	def EnterInflate(self):
		self.FeedbackOn()
		self.count = 0
		self.state_start_time = time.time()

	def ExitInflate(self):
		return

	def ForceDeflate(self):
		if time.time() - self.state_start_time > self._force_deflate_time:
			return 'Off'
		else:
			return 'ForceDeflate'

	def EnterForceDeflate(self):
		self.FeedbackOff()
		self.state_start_time = time.time()

	def ExitForceDeflate(self):
		return


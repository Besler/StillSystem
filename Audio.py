import vlc

class Audio:
	def __init__(self, filename):
		self.player = vlc.MediaPlayer(filename)
		self.player.play()

	def Pause(self):
		self.player.set_pause(True)

	def Play(self):
		self.player.set_pause(False)

	def Stop(self):
		self.player.stop()

import pypboy
import config
import game
import pypboy.ui
from pypboy.modules.data import entities

class Module(pypboy.SubModule):

	label = "Radio"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		self.stations = [
			entities.GalaxyNewsRadio(),
			entities.RadioEnclave()
		]
		for station in self.stations:
			self.add(station)
		self.active_station = None
		self.menu = pypboy.ui.Menu(300, ["Off", "Galaxy News Radio", "Radio Enclave"], [self.stop_radio, self.play_gnr, self.play_enc], 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		config.radio = self
		self.add(self.menu)
		
		
	def stop_radio(self):
		print "Off"
		if hasattr(self, 'active_station') and self.active_station:
			self.active_station.stop()
		
	def play_gnr(self):
		print "GNR"
		self.select_station(0)
		self.active_station.render()

	def play_enc(self):
		print "Enclave"
		self.select_station(1)
		
	def select_station(self, station):
		if hasattr(self, 'active_station') and self.active_station:
			self.active_station.stop()
		self.active_station = self.stations[station]
		self.active_station.play_random()


	def handle_event(self, event):
		if event.type == config.EVENTS['SONG_END']:
			if hasattr(self, 'active_station') and self.active_station:
				self.active_station.play_random()

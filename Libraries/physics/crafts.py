from abc import ABC, abstractmethod
from mathematics import Vector

class Craft(ABC):
	@abstractmethod
	def __init__(self, name = "", mass = 0, location = Vector((0,0,0)), controller):
		self.name = name
		self.mass = mass
		self.location = location
		self.controller = controller
	@abstractmethod
	def getSpeed(self, time, force):
		pass
	
	def gForce(self, gField):

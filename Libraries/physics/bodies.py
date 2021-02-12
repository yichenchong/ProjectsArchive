from mathematics import Vector

# general functions
g = 6.67408E-11
defaultStepSize = 0.1

class Body:
	def __init__(self, mass, velocity = Vector((0,0,0)), location = Vector((0, 0, 0)), name = ""):
		self.size=0
		self.__mass=mass
		self.velocity=velocity
		self.location=location
		self.acceleration=0
	def changeSize(newSize):
		self.size = newSize
	def rename(newName):
		self.name = newName
	def mass():
		return self.__mass
	def fgOn(self, body2):
		# calculates the force of gravity of self on another body
		distance = self.location.distance(body2.location)
		if distance == 0:
			return Vector((0,0,0))
		magnitude = self.__mass * body2.mass() * g / (distance ** 2)
		direction = self.location - body2.location
		return Vector.convert(magnitude, direction)
	def acceleration(self, force):
		return force / self.mass
	def velocity(self, force=0, stepSize=defaultStepSize):
		self.velocity += self.acceleration(force) * stepSize
		return self.velocity
	def position(self, force=0, stepSize=defaultStepSize):
		self.location += self.velocity(force, stepSize) * stepSize
		return self.location


class System(Body):
	def __init__(self):
		self.bodies = []
	def update(stepSize = defaultStepSize, externalForces = {}):
		for index, i in enumerate(self.bodies):
			netForce = Vector((0,0,0)) if index not in externalForces else externalForces[index]
			for j in self.bodies:
				netForce += j.fgOn(i)
			i.position(netForce, stepSize)
	def mass():
		return sum([i.mass() for i in self.bodies])
	def centerM():
		netsum = Vector((0,0,0))
		weightedMasses = [i.mass() * i.location for i in self.bodies]
		for i in weightedMasses:
			netsum += i
		return netsum / self.mass()
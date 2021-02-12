class Vector:
	def __init__(self, value):
		self.value = value
	def __add__(self, y):
		# adds two vectors together
		return Vector(tuple([(self.value[i] + y.value[i]) for i in range(len(self.value))]))
	def __sub__(self, y):
		# subtracts a vector from another vector
		return Vector(tuple([(self.value[i] - y.value[i]) for i in range(len(self.value))]))
	def __mul__(self, y):
		# multiplies a vector by a scalar
		return Vector(tuple([i * y for i in self.value]))
	def __div__(self, y):
		# divides a vector by a scalar
		return Vector(tuple([i / y for i in self.value]))
	def magnitude(self):
		# returns the overall magnitude of the vector
		return sum([i ** 2 for i in self.value]) ** 0.5
	def distance(self, y):
		# returns the distance between the coordinate and another coordinate
		return sum([(self.value[i] - y.value[i]) ** 2 for i in range(len(self.value))]) ** 0.5
	def __eq__(self, y):
		return self.value == y.value
	def __ne__(self, y):
		return not (self == y)
	def __lt__(self, y):
		return self.magnitude() < y.magnitude()
	def __le__(self, y):
		return self.magnitude() <= y.magnitude()
	def __gt__(self, y):
		return not (self <= y)
	def __ge__(self, y):
		return not (self < y)
	@staticmethod
	def convert(magnitude, direction):
		# converts a magnitude and direction into a Vector object
		dUV = direction / direction.magnitude()
		return Vector(dUV * magnitude)
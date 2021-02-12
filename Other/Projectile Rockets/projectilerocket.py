# set up libraries
import math

# default values
vi  = 2235.2
ac =  1.5
cd = 0.04
m =  800
stepsize = 0.001

# constant values
g = 3.985760576E14 # earth gravitational constant, derived by the mass of earth multiplied by the gravitational constant
c = 0.9999038507764790564367483932521666046654 # drag exponential, the factor of how air thins through the atmosphere, calculated by 1 / e ^ (1 / Hn)
r = 6371000 # radius of earth
b = 0.61251
"""For more information, b is calculated to be (ac * cd * M * p0)/(2 * R * T)"""

# functions used for calculating
def acc(h, v, ac = ac, cd = cd, m = m):
	return -1 * (g * h ** -2 + (b * ac * cd) * (c ** (h - r)) * (v ** 2) / m)
def iterate(t, h, v, a, ac = ac, cd = cd, m = m, stepsize = stepsize):
	t += stepsize
	h += v * stepsize
	v += a * stepsize
	a = acc(h, v, ac, cd, m)
	return t, h, v, a


# calculating final output
def resultant(vi = vi, ac = ac, cd = cd, m = m,  stepsize = stepsize):
	"""
		Function Resultant
		Inputs:
			vi - launch velocity in meters per second
			ac - surface area in contact with air (for drag calculations) in sq. meters
			cd - drag coefficient
			m - projectile mass
		Output: tuple with time and distance travelled of highest point
	"""

	# init conditions
	v, h, t = vi, r, 0
	a = acc(h,v,ac,cd,m)

	# execute loop
	while v > 0:
		t, h, v, a = iterate(t, h, v, a, ac, cd, m, stepsize)
	return (t, h - r)

def flightpath(vi = vi, ac = ac, cd = cd, m = m,  stepsize = stepsize):
	"""
		Function FlightPath
		Inputs:
			vi - launch velocity in meters per second
			ac - surface area in contact with air (for drag calculations) in sq. meters
			cd - drag coefficient
			m - projectile mass
		Output: array of tuples of time and heights
	"""
	# init conditions
	v, h, t = vi, r, 0
	a = acc(h,v,ac,cd,m)
	path = [(t, 0)]

	# execute loop
	while v > 0:
		t, h, v, a = iterate(t, h, v, a, ac, cd, m, stepsize)
		path.append((t, h - r))
	return path





# loop if run as script
if __name__ == '__main__':

	# init conditions
	v, h, t = vi, r, 0

	a = acc(h,v)

	# define printing
	def readout():
		print("At t = " + str(t) + ", " + str(h - r) + " m altitude, at " + str(v) + " mps and is experiencing a deceleration of " + str(a))
	readout()

	# execution loop
	while v > 0:
		t, h, v, a = iterate(t, h, v, a)
		readout()
	print("The rocket reached its maximum height of about " + str(h - r) + " sometime between " + str(t - stepsize) + " and " + str(t) + " seconds")
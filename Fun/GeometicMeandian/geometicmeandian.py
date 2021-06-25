def geometricMean(*args):
	product = 1
	n = len(args)
	for i in args:
		product *= i
	return product ** (1/float(n))

def arithmeticMean(*args):
	return sum(args)/len(args)

def median(*args):
	n = len(args)
	args = list(args)
	args.sort()
	if len(args) % 2 == 0:
		return (args[n//2-1] + args[n//2]) / 2
	else:
		return args[n//2]

def harmonicMean(*args):
	if len(args) == 0:
		return 0
	sum_num = 0
	for i in args:
		sum_num += (1/float(i))
	return len(args)/sum_num

def hybrid(precision, functions, *args):
	if len(args) == len(functions) and max(args) - min(args) < precision:
		average = sum(args)/len(args)
		error = max(max(args) - average, average - min(args))
		return str(average) + "±" + str(error)
	fList = []
	for f in functions:
		fList.append(f(*args))
	print(fList)
	return hybrid(precision, functions, *fList)

hybridsDict = { "gmdn": (arithmeticMean, geometricMean, median),
				"pyth": (arithmeticMean, geometricMean, harmonicMean),
				"soup": (arithmeticMean, geometricMean, harmonicMean, median)
				}
def gmdn(precision, *args):
	return hybrid(precision, hybridsDict["gmdn"], *args)
def pyth(precision, *args):
	return hybrid(precision, hybridsDict["pyth"], *args)
def soup(precision, *args):
	return hybrid(precision, hybridsDict["soup"], *args)

def test(testSet, testPrecision):
	print("Test set: " + str(testSet))
	print("")
	print("Testing means - ")
	print("Geometric mean: ", geometricMean(*testSet))
	print("Arithmetic mean: ", arithmeticMean(*testSet))
	print("Median: ", median(*testSet))
	print("Harmonic mean: ", harmonicMean(*testSet))
	print("")
	print("gmdn: ", gmdn(testPrecision, *testSet))
	print("pyth: ", pyth(testPrecision, *testSet))
	print("soup: ", soup(testPrecision, *testSet))
	print("\n\n")

testSet = (1, 1, 2, 3, 5)
testPrecision = 0.0000005
test(testSet, testPrecision)
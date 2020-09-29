# Initialized variable - no type needed
hello = "Hello World!"
singleQuotes = 'JD'
number = 1;	# Semicolon doesn't seem to be a problem
boo = True	#True/False (capital letter)

# Uninitialized variable - specified type
uninitialized:float
uninitialized = 1.2

# Sample tuple (immutable)
programming_languages = "C#", "VB.NET", "C++", "Java", "Python"

# type == .NET's typeof; prints 'tuple'
print(type(programming_languages))

print(uninitialized)

# Print formats - important!
print("Integer %d, floating point %f, string %s" % (1, 1.0, "1"))

# Input
userInput = input("Enter something! ")

# If else
if (True):
	print("True!")
else:
	print("False!")

# Loops
# Do note - the indent is necessary!
for language in programming_languages:
	print(language)

# Sample list (mutable)
numbers = [0,1,2,3,4]

# 2D list
game = [[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8]]

for g in game:
	print(g)

# For loop with 2 variables and enumerate (returns count and sequence)
for count,row in enumerate(game):
	print(count,row)

# Functions
def make_calculation():
	print("make_calculation function!")

def raise_to_power(num:int, pow = 2):
	result = 1
	for i in range (0,pow):
		result = result * num
	return result

# prints 27
print(raise_to_power(3,3))

# *name = .NET's params[]
def second_element(*name):
	print(name[2])

# prints "trzy"
second_element("jeden", "dwa", "trzy")

# Recursion - nothing new
def fib_recursive(n):
	if (n < 2):
		return n
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(7))

# Lambda expressions (anonymous functions)
x = lambda a: a + 1
print(x(5))

# Classes
class Point:
	def __init__(self, x:float, y:float):	# Constructor (self is the instance of the class)
		self.X = x
		self.Y = y
	X:float
	Y:float

	def ToString(self):	# Again, self is used to refernce the instance and its properties; it doesn't need to be called self, but has to be the first parameter
		print("Point @ (%.2f, %.2f)" % (self.X, self.Y))

	def Xd(xdObj):
		print("xdObj.X = %.2f" % xdObj.X)

p1 = Point(1,2)
p1.ToString()
p1.X = 3.5
p1.Xd()

# Delete a property from an object
del p1.X
# print(p1.X) - error! no X property

# Delete object
del p1

# Inheritance
class Point3D(Point):
	Z:float

	# By default, the constructor is overriden - but we can call the base class' constructor for the base class explicitly
	def __init__(self, x:float, y:float, z:float):
		Point.__init__(self,x,y)
		self.Z=z

p2 = Point3D(1,2,3)
p2.ToString()

# .NET's DateTime
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%d/%m/%y %H:%M"))

# Maths
import math

min = min(1,2,3)
max = max(1,2,3)

absoluteValue = abs(-13)

power = pow(13,4)

# Raise to power, then modulo the result
res = pow(13,4,1)

PI = math.pi

# try-except = .NET's try-catch
try:
	print(undefinedValue)
except:
	print("Tried to print undefined value!")
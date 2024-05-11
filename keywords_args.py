def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, *args):
		# access args index like array does
		self.speed = args[0]
		self.color = args[1]


# creating objects of car class
audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)

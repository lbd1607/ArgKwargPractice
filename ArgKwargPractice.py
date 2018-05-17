#Laura Davis
#This program demonstrates args and kwargs in Python

def ArgFunc(*args):
	for arg in args:
		print arg
		
#Func(1,2,3,4,5,"ham")
x = [1,2,3,4,5,"ham"]
#Func(*x)

def Func(x = 234, y = 9):
	print x, y
	
#Func(x = 3, y * 2)

def KFunc(**kwargs):
	for item in kwargs.items():
		print item
		
#KFunc(x = 456, y = 3)

def Combo(*args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item
		
Combo(x = 22, y = 256)
	


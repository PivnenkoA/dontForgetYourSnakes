"""Rus. Основные типы данных.
Eng. Basic data types
"""
def stringData():
	"""Rus. Это строка.
	Eng. This is a string.
	"""
	robot = "I am a robot. I'm here to kill all humans!"
	print(stringData.__doc__)
	print(robot)
	print(type(robot))
	
def integerData():
	"""Rus. Это целое число.
	Eng. This is a integer.
	"""
	num = 42
	print(integerData.__doc__)
	print(num)
	print(type(num))
	
def floatData():
	"""Rus. Это число с плавающей точкой.
	Eng. This is a float.
	"""
	pi = 3.141592
	print(floatData.__doc__)
	print(pi)
	print(type(pi))
	
def listData():
	"""Rus. Это списки.
	Eng. This are lists.
	"""
	animals = ['Lion', 'Python', 'Mouse']
	numbers = [42, 7, 2]
	print(listData.__doc__)
	print(animals)
	print(numbers)
	print(type(animals), type(numbers))
	
def tupleData():
	"""Rus. Это кортеж.
	Eng. This is a tuple.
	"""
	predators = ('Lion', 'Python', 'Wolf')
	print (tupleData.__doc__)
	print (predators)
	print(type(predators))
	
def dictionaryData():
	"""Rus. Это словарь.
	Eng. This is a dictionary.
	"""
	myDict = {'Смысл жизни':42, 'Число пи':3.141592, 42:101010}
	print(dictionaryData.__doc__)
	print(myDict)
	print(type(myDict))
	
def booleanData():
	"""Rus. Это логический (булевой/boolean) тип данных.
	Eng. This is a boolean type of data.
	"""
	t = 100>99
	f = 33 == 58
	print(booleanData.__doc__)
	print(t,f)
	print(type(t), type(f))

if __name__ == "__main__":
	print(__doc__)
	stringData()
	integerData()
	floatData()
	listData()
	tupleData()
	dictionaryData()
	booleanData()
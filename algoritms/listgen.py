"""Генератор списков случайных чисел.
Generator of random numbers lists"""
from random import randint


def listgen(length,minimum,maximum):
	ls =[]
	for i in range(length):
		di = randint(minimum,maximum)
		ls.append(di)
	return ls
	
if __name__ == "__main__":
	print(__doc__)
	print(listgen(99,5,24))
	
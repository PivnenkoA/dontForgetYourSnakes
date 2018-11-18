"""Классика сортировки массивов. Пузырьковая сортировка.
Classic of array sort. Bubble sort."""
from random import randint



def bubble (ls):
	n = 1
	while n <= len(ls):
		for i in range(len(ls)-n):
			if ls[i] < ls[i+1]:
				ls[i],ls[i+1] = ls[i+1],ls[i]
		n += 1
	return ls
		
def listgen(length):
	ls =[]
	for i in range(length):
		di = randint(1,9999)
		ls.append(di)
	return ls

if __name__ == "__main__":
	print(__doc__)
	ar = listgen(50)
	print("+++Not sort list+++")
	print(ar)
	
	print('+++Sort list+++')
	print(bubble(ar))
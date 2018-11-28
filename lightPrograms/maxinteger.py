"""Во многих языках программирования, целые числа ограничены битностью системыю. 
Вычислить максимальное или минимальное (отрицательное) значение целого числа 
не сложно. Если, конечно, Вы пользуетесь Python3.
In many programming languages, integers are limited by the system’s bit. 
Calculate the maximum or minimum (negative) value of an integer is not 
difficult. If, of course, you use Python 3"""
from platform import architecture



def maxAndMin(bits):
	"""Похожая функция есть в модуле sys (sys.maxsize). Но так же не интересно...
A similar function is in the module sys (sys.maxsize). But so not interesting ..."""
	temp = (2**bits)/2
	maxint = int(temp)-1
	minint = (maxint+1)*(-1)
	maxmin = [maxint,minint]
	return maxmin
	
if __name__ == "__main__":
	arch = architecture()[0]
	bitsys = int(arch[0:2])
	instans = maxAndMin(bitsys)
	print(__doc__)
	print("---"*20,'\n',"min =",str(instans[1]),'max =',str(instans[0])+'\n'+"---"*20)
	print(maxAndMin.__doc__)
	
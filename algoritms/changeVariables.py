"""Два алгоритма изменения заначения переменных
Two algorithms for change variables value"""
def change(a,s):
	"""Не самый простой, но самый очевидный способ."""
	print('a =',str(a),'s =',str(s))
	d = a
	a = s
	s = d
	print('a =',str(a),'s =',str(s))
def changePy(a,s):
	"""Feel the power of Python"""
	print('a =',a,'s =',s)
	(a,s)=(s,a)
	print('a =',a,'s =',s)
	
def changeBonus(a,s):
	"""+++Бонус+++ Не пользуйтесь этим способом!
	+++Bonus+++ Do not use this method!"""
	print('a =',a,'s =',s)
	q = a
	w = s
	s = q
	a = w
	print('a =',a,'s =',s)
	
if __name__ == "__main__":
	print(__doc__)
	print(change.__doc__)
	change(42,7)
	print(changePy.__doc__)
	changePy(57,23)
	print(changeBonus.__doc__)
	changeBonus(99,177)
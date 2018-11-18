"""Rus. Рассмотрим конструкции ветвления.
Eng. Consider the design of the branch.
"""



def constructionIf(a,s):
	"""Rus. Простая конструкция if-else.
	Eng. Simle constuction if-else.
	"""
	if a>s:
		print("Истину глаголишь!\nYou are speaking the truth!")
	else:
		print("Ты всё врёшь!\nYou're lying!")
		
def constructionElif(a,s):
	if a>s:
		print("Первое больше Второго")
	elif a<s:
		print("Второе больше первого")
	else:
		print("Не чё не пойму. Они, что равны?")
	
	
if __name__ == "__main__":
	print(__doc__)
	print('Какую конструкцию Вы хотите рассмотреть?')
	q = input('Если if-else введите 1\nЕсли if-elif-else введите 2\n')

	if q == '1':
		a = input('input value of the first variable: ')
		s = input('input value of the second variable: ')
		constructionIf(a,s)
	elif q == '2':
		a = input('input value of the first variable: ')
		s = input('input value of the second variable: ')
		constructionElif(a,s)
	else:
		print('Всё пропало!!! Не верное значение!!!')
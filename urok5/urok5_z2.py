print('Введите слово')
word = input()
a = word.count('a')
e = word.count('e')
i = word.count('i')
o = word.count('o')
u = word.count('u')
sum = int(len(word))
g = (a + e + i + o + u)
s = sum - g
if a <= 0 or e <= 0 or i <= 0 or o <= 0 or u <= 0:
	print(False)
else:
    print(f'Согласных: {s}'
		  f'\nГласных: {g}'
		  f'\na: {a}'
		  f'\ne: {e}'
		  f'\ni: {i}'
		  f'\no: {o}'
		  f'\nu: {u}')
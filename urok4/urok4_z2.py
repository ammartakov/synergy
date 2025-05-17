print('Введите целое пятизначное число')
inlet = input()
if len(inlet) == 5:
    a, b, c, d, e = map(int, inlet)
    if a == b and b == c and c == d and d == e:
        print('Все числа одинаковые, делить на 0 нельзя')
        exit()
    r = (((d ** e) * c) / (a - b))
    print(f'Ответ: {r}')
else:
    print('Введено не пятизначное число')
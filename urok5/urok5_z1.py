print('Введите число')
num = int(input())
if num < 0 and num % 2 == 0:
    print('Отрицательное четное число')
elif num > 0 and num % 2 == 1:
    print('Положительное не четное число')
elif num < 0 and num % 2 == 1:
    print('Отрицательное не четное число')
elif num > 0 and num % 2 == 0:
    print('Положительное четное число')
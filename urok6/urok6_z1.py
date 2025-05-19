print('Введите количество чисел')
n = int(input())
zero = 0
c = 0
while n > 0:
    print('Введите число')
    c = int(input())
    if c == 0:
        zero += 1
    n -= 1
print(f'Количество введенных нулей: {zero}')
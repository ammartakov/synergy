print('Введите число A')
a = int(input())
print('Введите число B (больше или равно A)')
b = int(input())
if a > b:
    print('A должно быть меньше B')
else:
    if a % 2 != 0:
        a += 1

    result = ''
    for i in range(a, b + 1, 2):
        result += str(i) + ' '

    print(f'Четные числа отрезка: {result.strip()}')
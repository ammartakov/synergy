x = int(input('Введите натуральное число: '))
count = 0
i = 1
while i * i <= x:
    if x % i == 0:
        if i * i == x:
            count += 1
        else:
            count += 2
    i += 1
print(f'Количество делителей для {x}: {count}')
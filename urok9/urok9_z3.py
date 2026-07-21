print('Введите числа через пробел')
s = input()
numbers = s.split()

seen = set()

for num_str in numbers:
    num = int(num_str)
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
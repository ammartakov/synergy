n = int(input("Введите количество чисел: "))
s = input("Введите числа через пробел: ")
numbers = s.split()
distinct_numbers = set()  # Используем set для хранения уникальных чисел

for num_str in numbers:
    num = int(num_str)
    distinct_numbers.add(num)

print("Количество различных чисел:", len(distinct_numbers))
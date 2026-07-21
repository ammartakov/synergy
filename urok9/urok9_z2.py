first_list = []
print('Вводите числа для первого списка, каждое на отдельной строке. После ввода первого списка нажмите Enter, чтобы ввести пустую строку.')
while True:
    try:
        line = input()
        if not line:
            break
        first_list.append(int(line))
    except EOFError:
        break

second_list = []
print('Вводите числа для второго списка, каждое на отдельной строке. После ввода второго списка нажмите Enter, чтобы ввести пустую строку.')
while True:
    try:
        line = input()
        if not line:
            break
        second_list.append(int(line))
    except EOFError:
        break

first_set = set(first_list)
second_set = set(second_list)

intersection = first_set.intersection(second_set)

print(len(intersection))
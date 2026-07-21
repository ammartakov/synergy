print('Введите строку без пробелов')
line = input()
inv_line = line[::-1]
if line == inv_line:
    print('yes')
else:
    print('no')
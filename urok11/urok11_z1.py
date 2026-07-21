def factorial_list(n):

    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x-1)

    n_factorial = factorial(n)

    factorial_sequence = []
    current_number = n_factorial

    while current_number > 0:
        factorial_sequence.append(factorial(current_number))
        current_number -= 1

    return factorial_sequence

number = int(input("Введите натуральное целое число: "))
result = factorial_list(number)
print(result)
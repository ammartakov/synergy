import random
import string

def generate_string_with_random_spaces(length):
    result = ""
    space_locations = sorted(random.sample(range(1, length), random.randint(0, length - 1)))

    if not space_locations:
        return " " * length

    last_space_location = 0
    for space_location in space_locations:
        result += " " * (space_location - last_space_location) + random.choice(string.ascii_letters)
        last_space_location = space_location

    result += " " * (length - last_space_location)

    return result

length = 1000
random_string = generate_string_with_random_spaces(length)
print(f'Строка:'
      f'\n{random_string}')
print(len(random_string))

result = ' '.join(random_string.split())
print(f'Результат объединения:'
      f'\n{result}')
print(len(result))
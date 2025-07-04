pets = {}

while True:
    pet_name = input("Введите имя питомца (или 'стоп' для завершения): ")
    if pet_name.lower() == 'стоп':
        break

    pet_type = input("Введите вид питомца: ")
    while True:
      try:
        pet_age = int(input("Введите возраст питомца: "))
        break
      except ValueError:
        print("Возраст должен быть целым числом.")

    owner_name = input("Введите имя владельца: ")

    pets[pet_name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

for pet_name, pet_info in pets.items():
    age = pet_info["Возраст питомца"]
    if age % 10 == 1 and age % 100 != 11:
      years_str = "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
      years_str = "года"
    else:
      years_str = "лет"

    print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age} {years_str}. Имя владельца: {pet_info["Имя владельца"]}')
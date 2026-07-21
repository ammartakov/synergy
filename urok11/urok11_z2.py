import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    },
}


def get_pet(ID):
    return pets[ID] if ID in pets else False


def get_suffix(age):
    age = int(age)
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"


def pets_list():
    if not pets:
        print("В базе данных питомцев нет.")
        return

    print("Список питомцев:")
    for ID, pet_data in pets.items():
        for pet_name, pet_info in pet_data.items():
            print(f"{ID}: {pet_name} ({pet_info['Вид питомца']})")


def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    while True:
        try:
            pet_age = int(input("Введите возраст питомца: "))
            break
        except ValueError:
            print("Некорректный ввод. Возраст должен быть целым числом.")
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец {pet_name} успешно добавлен с ID {new_id}.")


def read():
    while True:
        try:
            pet_id = int(input("Введите ID питомца: "))
            break
        except ValueError:
            print("Некорректный ввод. ID должен быть целым числом.")

    pet_data = get_pet(pet_id)

    if not pet_data:
        print("Питомца с таким ID не существует.")
        return

    for pet_name, pet_info in pet_data.items():
        age = pet_info["Возраст питомца"]
        suffix = get_suffix(age)
        print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age} {suffix}. Имя владельца: {pet_info["Имя владельца"]}')


def update():
    while True:
        try:
            pet_id = int(input("Введите ID питомца для обновления: "))
            break
        except ValueError:
            print("Некорректный ввод. ID должен быть целым числом.")

    pet_data = get_pet(pet_id)

    if not pet_data:
        print("Питомца с таким ID не существует.")
        return

    for pet_name in pet_data.keys():
        print(f"Редактирование питомца {pet_name}:")

        new_pet_type = input(f"Введите новый вид питомца (оставьте пустым, чтобы не менять): ")
        new_pet_age_str = input(f"Введите новый возраст питомца (оставьте пустым, чтобы не менять): ")
        new_owner_name = input(f"Введите новое имя владельца (оставьте пустым, чтобы не менять): ")

        if new_pet_type:
            pets[pet_id][pet_name]["Вид питомца"] = new_pet_type

        if new_pet_age_str:
            try:
                new_pet_age = int(new_pet_age_str)
                pets[pet_id][pet_name]["Возраст питомца"] = new_pet_age
            except ValueError:
                print("Некорректный ввод. Возраст не был обновлен.")

        if new_owner_name:
            pets[pet_id][pet_name]["Имя владельца"] = new_owner_name

        print("Информация о питомце успешно обновлена.")


def delete():
    while True:
        try:
            pet_id = int(input("Введите ID питомца для удаления: "))
            break
        except ValueError:
            print("Некорректный ввод. ID должен быть целым числом.")

    if pet_id not in pets:
        print("Питомца с таким ID не существует.")
        return

    del pets[pet_id]
    print("Запись о питомце успешно удалена.")


while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ").lower()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        break
    else:
        print("Некорректная команда.")

print("Программа завершена.")
from datetime import datetime

# Словарь с цифрами в формате электронного табло (5x3)
DIGITS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        " *** ",
        "*   *",
        "   * ",
        "  *  ",
        "*****"
    ],
    '3': [
        " *** ",
        "*   *",
        "   * ",
        "*   *",
        " *** "
    ],
    '4': [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    '5': [
        "*****",
        "*    ",
        "***  ",
        "   * ",
        "***  "
    ],
    '6': [
        " *** ",
        "*    ",
        "**** ",
        "*   *",
        " *** "
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   "
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        " ****",
        "    *",
        " *** "
    ]
}

def get_weekday(day, month, year):
    """Определяет день недели для заданной даты"""
    try:
        date = datetime(year, month, day)
        weekdays = ['Понедельник', 'Вторник', 'Среда', 
                    'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        return weekdays[date.weekday()]
    except ValueError:
        return None

def is_leap_year(year):
    """Определяет, является ли год високосным"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    """Рассчитывает возраст пользователя"""
    today = datetime.now()
    birth_date = datetime(year, month, day)
    
    age = today.year - birth_date.year
    
    # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def print_number_stars(number):
    """Выводит число в формате электронного табло"""
    # Преобразуем число в строку
    num_str = str(number)
    
    # Для каждой строки из 5 строк табло
    for row in range(5):
        line = ""
        for digit in num_str:
            if digit in DIGITS:
                line += DIGITS[digit][row] + "  "  # добавляем пробел между цифрами
            else:
                line += "     "  # для неизвестных символов
        print(line)

def main():
    print("=" * 50)
    print("Программа стилистического преобразования чисел")
    print("=" * 50)
    
    # Запрос данных у пользователя
    while True:
        try:
            day = int(input("Введите день рождения (1-31): "))
            month = int(input("Введите месяц рождения (1-12): "))
            year = int(input("Введите год рождения (например, 1990): "))
            
            # Проверка корректности даты
            date_check = get_weekday(day, month, year)
            if date_check is None:
                print("Ошибка: Неверная дата! Пожалуйста, введите корректную дату.\n")
                continue
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целые числа!\n")
    
    # Получаем информацию о дате
    weekday = get_weekday(day, month, year)
    leap = is_leap_year(year)
    age = calculate_age(day, month, year)
    
    # Выводим информацию
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)
    print(f"• День недели: {weekday}")
    print(f"• Високосный год: {'Да' if leap else 'Нет'}")
    print(f"• Возраст: {age} лет")
    
    # Выводим дату в стилизованном формате
    print("\n" + "=" * 50)
    print("Дата рождения в формате электронного табло:")
    print("=" * 50)
    
    # Форматируем день и месяц с ведущими нулями
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year}"
    
    # Выводим каждую часть
    print("\nДень:")
    print_number_stars(day_str)
    
    print("\nМесяц:")
    print_number_stars(month_str)
    
    print("\nГод:")
    print_number_stars(year_str)
    
    # Альтернативный вариант - вывод одной строкой
    print("\n" + "=" * 50)
    print("Вся дата одной строкой:")
    print("=" * 50)
    
    full_date = f"{day_str}.{month_str}.{year_str}"
    # Для вывода одной строкой нужно модифицировать функцию
    for row in range(5):
        line = ""
        for char in full_date:
            if char == '.':
                line += "     "  # пробел для точки
            elif char in DIGITS:
                line += DIGITS[char][row] + "  "
            else:
                line += "     "
        print(line)

if __name__ == "__main__":
    main()
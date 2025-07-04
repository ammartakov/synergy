import random
import os
import pickle

# Константы
EMPTY = '⬛'
TREE = '🌳'
WATER = '🌊'
FIRE = '🔥'
HELICOPTER = '🚁'
HOSPITAL = '🏥'
CLOUD = '☁️ '
THUNDER = '⚡️'

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.helicopter_position = [0, 0]
        self.water_reservoirs = 1
        self.score = 0
        self.lives = 3
        self.tick_count = 0  # Счётчик тиков для периодических событий
        self.hospital_position = self.generate_random_cell()  # Случайная позиция госпиталя
        self.grid[self.hospital_position[1]][self.hospital_position[0]] = HOSPITAL  # Установка госпиталя

        # Генерация рек и деревьев
        self.generate_rivers()
        self.generate_trees()

        # Поджигаем случайное дерево в начале игры
        self.ignite_random_tree()

    def generate_rivers(self):
        num_rivers = random.randint(1, 3)
        for _ in range(num_rivers):
            river_length = random.randint(3, self.width // 2)  # Ограничение длины реки
            start_x = random.randint(0, self.width - river_length - 1)
            y_position = random.randint(0, self.height - 1)
            for x in range(start_x, start_x + river_length):
                self.grid[y_position][x] = WATER

    def generate_trees(self):
        num_trees = random.randint(self.width * self.height // 10, self.width * self.height // 5)
        for _ in range(num_trees):
            x, y = self.generate_random_empty_cell()
            self.grid[y][x] = TREE

    def generate_random_empty_cell(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == EMPTY:
                return x, y

    def generate_random_cell(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return x, y

    def ignite_random_tree(self):
        trees_positions = [(y, x) for y in range(self.height) for x in range(self.width) if
                           self.grid[y][x] == TREE]
        if trees_positions:
            tree_to_ignite = random.choice(trees_positions)
            print(f"Дерево загорелось на позиции: {tree_to_ignite}")
            self.grid[tree_to_ignite[0]][tree_to_ignite[1]] = FIRE

    def display_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in range(self.height):
            line = ''
            for col in range(self.width):
                if [col, row] == self.helicopter_position:
                    line += HELICOPTER + ' '
                else:
                    line += self.grid[row][col] + ' '
            print(line)
        print(f"💰: {self.score} | ❤️: {self.lives} | 🌊: {self.water_reservoirs}")

    def move_helicopter(self, direction):
        x, y = self.helicopter_position
        new_x, new_y = x, y

        if direction == 'up':
            new_y = max(0, y - 1)
        elif direction == 'down':
            new_y = min(self.height - 1, y + 1)
        elif direction == 'left':
            new_x = max(0, x - 1)
        elif direction == 'right':
            new_x = min(self.width - 1, x + 1)
        # Если позиция изменилась
        if (new_x, new_y) != (x, y):
            self.helicopter_position = [new_x, new_y]

    def check_cell(self):
        x, y = self.helicopter_position  # Correct order
        current_cell_value = self.grid[y][x]

        # Пополнение воды
        if current_cell_value == WATER:
            print("Вы пополнили запасы воды!")
            self.water_reservoirs += 1

        # Тушение пожара
        elif current_cell_value == FIRE:
            if self.water_reservoirs > 0:
                print("Вы потушили пожар!")
                self.grid[y][x] = EMPTY
                self.water_reservoirs -= 1
                self.score += 10
                print(f"Вы получили 10 очков! Текущий счет: {self.score}")
            else:
                print("Недостаточно воды для тушения пожара.")

        # Посещение госпиталя
        elif current_cell_value == HOSPITAL:
            print("Вы посетили госпиталь!")
            heal_cost = 20  # Стоимость лечения
            if self.score >= heal_cost:
                self.score -= heal_cost
                self.lives = 3  # Полное восстановление здоровья
                print(f"Вы восстановили здоровье! Текущий счет: {self.score}")
            else:
                print("Недостаточно очков для лечения.")

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def tick(self):
        self.tick_count += 1

        new_fire_positions = []

        # Распространение огня
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == FIRE:
                    # Проверяем соседние клетки
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if (dx == 0 and dy == 0) or not self.is_valid_position(x + dx, y + dy):
                                continue  # Пропускаем саму клетку и невалидные позиции

                            if self.grid[y + dy][x + dx] == TREE and random.random() < 0.5:  # Вероятность возгорания
                                print(f"Огонь перекинулся на дерево в клетке ({x + dx}, {y + dy})")
                                new_fire_positions.append((x + dx, y + dy))
        # Применяем новые очаги возгорания
        for x, y in new_fire_positions:
            self.grid[y][x] = FIRE

        # Погодные явления (облака и грозы)
        if self.tick_count % 15 == 0:
            self.generate_clouds()
        if self.tick_count % 30 == 0:
            self.strike_lightning()

        # Рост деревьев (периодически)
        if self.tick_count % 20 == 0:
            self.grow_trees()

        # Автоматическое возгорание деревьев (периодически)
        if self.tick_count % 25 == 0:
            self.ignite_random_tree()

    def generate_clouds(self):
        x, y = self.generate_random_cell()
        print(f"В небе появились облака в районе ({x}, {y})")
        self.display_message(f"В небе появились облака в районе ({x}, {y})")
        self.grid[y][x] = CLOUD  # Обозначение для облака, если нужно отображать

    def strike_lightning(self):
        x, y = self.generate_random_cell()
        print(f"Молния ударила в клетку ({x}, {y})!")
        self.display_message(f"Молния ударила в клетку ({x}, {y})!")
        if self.grid[y][x] == TREE:
            print("Дерево загорелось от молнии!")
            self.display_message("Дерево загорелось от молнии!")
            self.grid[y][x] = FIRE

    def grow_trees(self):
        for _ in range(random.randint(1, 3)):  # Выращиваем несколько деревьев за раз
            x, y = self.generate_random_empty_cell()
            self.grid[y][x] = TREE  # Выращиваем деревья только в пустых клетках
            print(f"Выросло новое дерево в клетке ({x}, {y})")

    def shop(self):
        while True:
            print("\nДобро пожаловать в магазин!")
            print("1. Дополнительный резервуар для воды (10 очков)")
            print("2. Выход из магазина")

            choice = input("Выберите действие: ")

            if choice == '1':
                cost = 10
                if self.score >= cost:
                    print("Покупка успешна!")
                    self.score -= cost
                    self.water_reservoirs += 1
                    print(f"Теперь у вас {self.water_reservoirs} резервуаров воды.")
                else:
                    print("Недостаточно очков!")
            elif choice == '2':
                break
            else:
                print("Некорректный выбор.")

    def save_game(self):
        try:
            with open('savegame.pkl', 'wb') as f:
                pickle.dump(self, f)
            print("Игра сохранена.")
            self.display_message("Игра сохранена!")
        except Exception as e:
            print(f"Ошибка при сохранении игры: {e}")
            self.display_message(f"Ошибка при сохранении игры: {e}")

    def load_game(self):
        try:
            with open('savegame.pkl', 'rb') as f:
                loaded_game = pickle.load(f)
                # Update current instance's attributes with loaded attributes
                self.__dict__.update(loaded_game.__dict__)
            print("Игра загружена.")
            self.display_message("Игра загружена!")
        except FileNotFoundError:
            print("Сохраненная игра не найдена.")
            self.display_message("Сохраненная игра не найдена. Начинаем новую игру.")
            return False  # Игра не была загружена
        except Exception as e:
            print(f"Ошибка при загрузке игры: {e}")
            self.display_message(f"Ошибка при загрузке игры: {e}")
        return True  # Игра была загружена успешно

    def display_message(self, message):
        print(message)


def main():
    while True:
        print("1. Начать новую игру")
        print("2. Загрузить сохраненную игру")
        choice = input("Выберите действие: ")

        if choice == '1':
            width = int(input("Введите ширину поля: "))
            height = int(input("Введите высоту поля: "))
            game = Game(width, height)
            break  # Выход из цикла выбора
        elif choice == '2':
            #Создаем game object чтобы был к чему применить load_game
            width = int(input("Введите ширину поля: "))
            height = int(input("Введите высоту поля: "))
            game = Game(width, height)
            if game.load_game():
                break
            else:
                print("Загрузка не удалась, начните новую игру.")
        else:
            print("Некорректный ввод.")

    while game.lives > 0:  # Играем, пока есть жизни
        game.display_grid()

        command = input("Введите команду (w/a/s/d для движения; t для тика; p для магазина; save для сохранения; q для выхода): ").lower()

        if command == 'q':
            break

        elif command == 'w':
            game.move_helicopter('up')
            game.check_cell()

        elif command == 's':
            game.move_helicopter('down')
            game.check_cell()

        elif command == 'a':
            game.move_helicopter('left')
            game.check_cell()

        elif command == 'd':
            game.move_helicopter('right')
            game.check_cell()

        elif command == "t":
            game.tick()

        elif command == "p":
            game.shop()

        elif command == 'save':
            game.save_game()

        elif command == 'load':
            game.load_game()

        else:
            print("Неизвестная команда")
        game.tick() #Тик после каждого действия

    print("Игра окончена!")

if __name__ == "__main__":
    main()

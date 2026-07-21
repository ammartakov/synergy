class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Черепашка переместилась вверх. Новые координаты: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Черепашка переместилась вниз. Новые координаты: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Черепашка переместилась влево. Новые координаты: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Черепашка переместилась вправо. Новые координаты: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Черепашка эволюционировала. Размер шага увеличен до {self.s}")

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print(f"Черепашка деградировала. Размер шага уменьшен до {self.s}")
        else:
            raise ValueError("Размер шага не может быть меньше или равен 0.")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y


turtle = Черепашка(0, 0, 2)  # Создаем черепашку в (0, 0) с шагом 2

turtle.go_right()  # Перемещаем вправо
turtle.go_up()  # Перемещаем вверх

turtle.evolve()  # Увеличиваем шаг

print(f"Минимальное количество ходов до (10, 10): {turtle.count_moves(10, 10)}")

try:
    turtle.degrade()
    turtle.degrade()
    turtle.degrade()  # Вызовет ошибку, так как s станет 0
except ValueError as e:
    print(e)
class Касса:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, X):
        self.amount += X
        print(f"Касса пополнена на {X}. Текущая сумма: {self.amount}")

    def count_1000(self):
        thousands = self.amount // 1000
        print(f"В кассе {thousands} целых тысяч.")

    def take_away(self, X):
        if self.amount >= X:
            self.amount -= X
            print(f"Из кассы изъято {X}. Текущая сумма: {self.amount}")
        else:
            raise ValueError("Недостаточно денег в кассе.")


kassa = Касса(5500)  # Создаем кассу с начальной суммой 5500
kassa.top_up(2000)  # Пополняем кассу на 2000
kassa.count_1000()  # Выводим количество тысяч
try:
    kassa.take_away(10000)  # Пытаемся забрать 10000 (вызовет ошибку)
except ValueError as e:
    print(e)
kassa.take_away(1500)  # Забираем 1500
kassa.count_1000()  # Снова выводим количество тысяч
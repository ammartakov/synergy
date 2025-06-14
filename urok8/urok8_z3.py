print('Введите грузоподъемность лодки кг')
m = int(input())
print('Введите количество рыбаков')
n = int(input())
weights = []
for _ in range(n):
    print(f'Введите вес рыбака {_ + 1}')
    weights.append(int(input()))
weights.sort()
left, right = 0, n - 1
boats = 0
while left <= right:
    if left == right:
        boats += 1
        break
    if weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1
print(f'Необходимое количество лодок: {boats}')
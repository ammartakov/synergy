n = int(input())
numbers = []
for _ in range(n):
  numbers.append(int(input()))
numbers.reverse()
for num in numbers:
  print(num)
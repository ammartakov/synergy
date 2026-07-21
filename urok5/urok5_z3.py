print('Минимальная сумма инвестицый')
min_sum_invest = float(input())
print('Баланс Майкла')
sum_mike = float(input())
print('Баланс Ивана')
sum_ivan = float(input())
if sum_mike >= min_sum_invest and sum_ivan >= min_sum_invest:
    print('2')
elif sum_mike >= min_sum_invest and sum_ivan < min_sum_invest:
    print('Mike')
elif sum_ivan >= min_sum_invest and sum_mike < min_sum_invest:
    print('Ivan')
elif sum_ivan < min_sum_invest and sum_mike < min_sum_invest and sum_mike + sum_ivan >= min_sum_invest :
    print('1')
elif sum_ivan < min_sum_invest and sum_mike < min_sum_invest and sum_mike + sum_ivan < min_sum_invest :
    print('0')
from random import randint

number_of_coins = int(input('Введите колличество монет: '))
coins = [randint(0,1) for _ in range(number_of_coins+1)]
print(coins)
count0 = 0
count1 = 0
for i in range(number_of_coins+1):
    if coins[i] > 0:
        count1 +=1
    else: count0 +=1
if count0>count1:
    print(count1)
else:
    print(count0)
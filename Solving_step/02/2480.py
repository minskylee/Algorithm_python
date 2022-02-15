dice = list(map(int, input().split()))

price = 0
if dice[0] == dice[1] and dice[1] == dice[2]:
    price = dice[0]*1000 + 10000
elif dice[0] == dice[1] or dice[1] == dice[2]:
    price = dice[1]*100 + 1000
elif dice[2] == dice[0]:
    price = dice[0]*100 + 1000
else:
    price = max(dice)*100
print(price)
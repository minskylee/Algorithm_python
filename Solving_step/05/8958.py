N = int(input())

for i in range(N):
    OX = input()

    score = 0
    count = 0
    for s in OX:
        if s == 'X':
            count = 0
        else:
            count += 1
            score += count
    print(score)

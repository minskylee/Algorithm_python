T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        a, b = input().split()
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 1
    num = 1
    for key in clothes:
        num *= clothes[key] + 1
    print(num - 1)

# https://www.acmicpc.net/problem/7568
# 덩치

N = int(input())
haw = []
for _ in range(N):
    haw.append(list(map(int, input().split())))

for i in haw:
    cnt = 1
    for j in haw:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end = ' ')
# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(lambda x: 0 if x=='B' else 1, input())))
min_cnt = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt_1 = 0
        cnt_2 = 0
        for a in range(8):
            for b in range(8):
                if arr[i+a][j+b] == (a+b)%2:
                    cnt_1 += 1
                if arr[i+a][j+b] != (a+b)%2:
                    cnt_2 += 1
            cnt = cnt_1 if cnt_1 < cnt_2 else cnt_2
        if min_cnt > cnt:
            min_cnt = cnt
print(min_cnt)


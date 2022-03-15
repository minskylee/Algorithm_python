# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수


N = int(input())
arr = [[0 for _ in range(10)] for _ in range(N)]
for i in range(1, 10):
    arr[0][i] = 1
for i in range(1, N):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][j+1]
        elif j == 9:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
print(sum(arr[N-1]) % 10**9)
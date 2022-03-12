# https://www.acmicpc.net/problem/1932
# 정수 삼각형


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N-1, 0, -1):
    for j in range(i):
        arr[i-1][j] += max(arr[i][j], arr[i][j+1])
print(*arr[0])
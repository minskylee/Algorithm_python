# https://www.acmicpc.net/problem/12865
# 평범한 배낭


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bag = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = arr[i-1]
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)
print(bag[-1][-1])

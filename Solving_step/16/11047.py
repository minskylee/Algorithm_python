# https://www.acmicpc.net/problem/11047
# 동전 0


N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
cnt = 0
start = N-1
while K > 0:
    for i in range(start, -1, -1):
        if K-arr[i] >= 0:
            start = i
            cnt_val = K//arr[i]
            K -= arr[i]*cnt_val
            cnt += cnt_val
            break
print(cnt)

# https://www.acmicpc.net/problem/2565
# 전깃줄


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
len_arr = len(arr)
dp = [0]*N
for i in range(len_arr):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    print(dp)
print(N-max(dp))
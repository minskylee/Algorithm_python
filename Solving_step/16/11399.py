# https://www.acmicpc.net/problem/11399
# ATM


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]
print(sum(dp))

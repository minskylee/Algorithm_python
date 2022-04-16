# https://www.acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열


N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
dp2 = [0]*N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
        if arr[(N-1)-i] > arr[(N-1)-j]:
            dp2[(N-1)-i] = max(dp2[(N-1)-i], dp2[(N-1)-j]+1)
for i in range(N):
    dp[i] += dp2[i]
print(max(dp))

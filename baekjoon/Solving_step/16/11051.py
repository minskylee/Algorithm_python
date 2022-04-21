# https://www.acmicpc.net/problem/11051
# 이항 계수 2

fac = [1]*10001
for i in range(1, 10001):
    fac[i] = i*fac[i-1]

N, K = map(int, input().split())
print((fac[N] // (fac[K] * fac[N - K]))%10007)

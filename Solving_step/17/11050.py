# https://www.acmicpc.net/problem/11050
# 이항 계수 1


def fac(n):
    if n == 0:
        return 1
    return n* fac(n-1)


N, K = map(int, input().split())
print(fac(N) // (fac(K) * fac(N - K)))

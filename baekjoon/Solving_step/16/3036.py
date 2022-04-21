# https://www.acmicpc.net/problem/3036
# 링

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
arr = list(map(int, input().split()))
A = arr[0]
for i in range(1, N):
    B = gcd(A, arr[i])
    print(f'{A//B}/{arr[i]//B}')
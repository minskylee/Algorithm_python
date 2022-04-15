# https://www.acmicpc.net/problem/2981
# 검문


import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
gcd_val = abs(arr[1] - arr[0])
for i in range(2, N):
    gcd_val = gcd(gcd_val , abs(arr[i] - arr[i-1]))
gcd_idx = int(gcd_val**0.5)
gcd_set = set()
for i in  range(2, gcd_idx + 1):
    if gcd_val % i == 0:
        gcd_set.add(i)
        gcd_set.add(gcd_val // i)
gcd_set.add(gcd_val)
gcd_lst = sorted(list(gcd_set))
print(*gcd_lst)
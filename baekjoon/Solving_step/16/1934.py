# https://www.acmicpc.net/problem/1934
# 최소공배수


import math

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
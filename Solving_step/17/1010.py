# https://www.acmicpc.net/problem/1010
# 다리 놓기


import sys
input = sys.stdin.readline
from math import factorial

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M)//(factorial(N)*factorial(M-N)))

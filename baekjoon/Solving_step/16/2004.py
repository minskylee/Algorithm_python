# https://www.acmicpc.net/problem/2004
# 조합 0의 개수


import sys
input = sys.stdin.readline
 
def count_two(x):
    cnt = 0
    while x > 0:
        x = x // 2
        cnt += x
    return cnt
 
def count_five(x):
    cnt = 0
    while x > 0:
        x = x // 5
        cnt += x
    return cnt
 
def count_zero(x, y):
    t = count_two(x) - count_two(y) - count_two(x-y)
    f = count_five(x) - count_five(y) - count_five(x-y)
    return min(t, f)

N, M = map(int, input().split())
print(count_zero(N, M))
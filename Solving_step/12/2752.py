# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3


import sys


input = sys.stdin.readline

c_arr = [0 for _ in range(10001)]

n = int(input())
for i in range(n):
    c_arr[int(input())] += 1
for i in range(10001):
    if c_arr[i]:
        for _ in range(c_arr[i]):
            print(i)
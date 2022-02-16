# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기2

import sys
input = sys.stdin.readline


N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x:(x[1], x[0]))
for a in xy:
    print(*a)
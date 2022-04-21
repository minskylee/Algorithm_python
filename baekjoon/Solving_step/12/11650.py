# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기


import sys
input = sys.stdin.readline


N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x:(x[0], x[1]))
for a in xy:
    print(*a)
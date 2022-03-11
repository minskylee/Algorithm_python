# https://www.acmicpc.net/problem/1149
# RGB거리


import sys
input = sys.stdin.readline


def sol(idx, v, sum_v):
    global min_val
    if idx == N:
        if min_val > sum_v:
            min_val = sum_v
        return
    if min_val < sum_v:
        return
    for i in range(3):
        if i != v:
            sol(idx+1, i, sum_v + arr[idx][i])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1] ,arr[i-1][2])
    arr[i][1] += min(arr[i-1][0] ,arr[i-1][2])
    arr[i][2] += min(arr[i-1][1] ,arr[i-1][0])
print(min(arr[N-1]))
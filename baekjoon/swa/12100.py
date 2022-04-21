# https://www.acmicpc.net/workbook/view/1152
# 2048 (Easy)

'''
# 상 하 좌 우를 움직일 수 있다.
# 공간이 비어있다면 해당 위치로 숫자를 당기고
# 같은 숫자라면 합친다
# 공간에 숫자가 이미 있다면, 그 다음칸까지 숫자를 당긴다.
# dfs로 반복한다.
'''

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def up(arr):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[p][j] == 0:
                    arr[p][j] = tmp
                elif arr[p][j] == tmp:
                    arr[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    arr[p][j] = tmp
    return arr


def down(arr):
    for j in range(n):
        p = n-1
        for i in range(n-2, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[p][j] == 0:
                    arr[p][j] = tmp
                elif arr[p][j] == tmp:
                    arr[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    arr[p][j] = tmp
    return arr


def left(arr):
    for i in range(n):
        p = 0
        for j in range(1, n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][p] == 0:
                    arr[i][p] = tmp
                elif arr[i][p] == tmp:
                    arr[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    arr[i][p] = tmp
    return arr


def right(arr):
    for i in range(n):
        p = n-1
        for j in range(n-2, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][p] == 0:
                    arr[i][p] = tmp
                elif arr[i][p] == tmp:
                    arr[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    arr[i][p] = tmp
    return arr


def bk(idx, arr):
    if idx == 5:
        return max(map(max, arr))
    return max(
        bk(idx+1, up(deepcopy(arr))),
        bk(idx+1, down(deepcopy(arr))),
        bk(idx+1, left(deepcopy(arr))),
        bk(idx+1, right(deepcopy(arr)))
        )


print(bk(0, arr))

# https://www.acmicpc.net/problem/15683
# 감시


'''
# 각 감시카메라의 조건에따라 카메라의 방향을 설정한다.
# 감시카메라의 방향을 정하는 재귀함수를 만든다
# 방향을 정했으면, 벽을 만나거나 인덱스에서 벗어나기 전 까지 감시영역을 넓힌다.
# 0의 갯수를 확인하고, 가장 작은 크기를 구한다.
'''

from copy import deepcopy

def bk(idx, arr):
    global min_danger
    if idx == len(camera_loc):
        danger_space = 0
        for a in arr:
            danger_space += a.count(0)
        min_danger = min(min_danger, danger_space)
        return
    for d_list in camera_dic[camera[idx]]:
        arr_tmp = deepcopy(arr)
        for d in d_list:
            search(camera_loc[idx][0], camera_loc[idx][1], dr[d], dc[d], arr_tmp)
        bk(idx+1, arr_tmp)


def search(r, c, _dr, _dc, arr):
    while 0 <= r+_dr < n and 0 <= c+_dc < m and arr[r+_dr][c+_dc] != 6:
        arr[r+_dr][c+_dc] = '#'
        r += _dr
        c += _dc


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr, dc = (1, 0, -1, 0), (0, 1, 0, -1)
camera_dic = [
    [],
    [[0], [1], [2], [3]],
    [(0, 2), (1, 3)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    [(0, 1, 2, 3)],
]
camera_loc, camera = [], []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            camera_loc.append((i, j))
            camera.append(arr[i][j])
min_danger = n*m
bk(0, arr)
print(min_danger)

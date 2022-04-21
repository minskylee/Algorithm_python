# https://www.acmicpc.net/problem/14502
# 연구소


'''
# 브루투스로 빈 칸에 벽을 3개 세우는 모든 경우를 찾음
# 해당 경우일 때 bfs를 돌림
'''
from collections import deque
from copy import deepcopy

def bk_wall(cnt, arr):
    if cnt == 3:
        bfs(deepcopy(arr))
        return 
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                bk_wall(cnt+1, arr)
                arr[i][j] = 0


def bfs(arr):
    global safe
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i, j))
    while queue:
        cr, cc = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr+d[0], cc+d[1]
            if 0 <= nr < n and 0 <= nc < m and not arr[nr][nc]:
                arr[nr][nc] = 2
                queue.append((nr, nc))
    safe_loc = 0
    for a in arr:
        safe_loc += a.count(0)
    safe = max(safe, safe_loc)
    return


n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
wall = [[0]*m for _ in range(n)]
safe = 0
bk_wall(0, arr)
print(safe)

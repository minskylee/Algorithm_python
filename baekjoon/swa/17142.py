# https://www.acmicpc.net/problem/17142
# 연구소 3


from collections import deque
from copy import deepcopy


def bk(idx, cr, cc, virus):
    global min_t
    if idx == m:
        min_t = min(min_t, bfs(virus, deepcopy(v)))
        return
    for r in range(cr, n):
        k = 0
        if r == cr:
            k = cc
        for c in range(k, n):
            if arr[r][c] == 2 and v[r][c] == -1:
                v[r][c] = 0
                bk(idx+1, r, c, virus+[(r, c)])
                v[r][c] = -1


def bfs(virus, v):
    queue = deque()
    for vv in virus:
        queue.append(vv)
    max_val = 0
    while queue:
        s = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = s[0]+d[0], s[1]+d[1]
            if 0 <= nr < n and 0 <= nc < n and v[nr][nc] == -1 and arr[nr][nc] != 1:
                v[nr][nc] = v[s[0]][s[1]] + 1
                if arr[nr][nc] == 0:
                    max_val = max(max_val, v[nr][nc])
                queue.append((nr, nc))
    a_cnt = 0
    v_cnt = 0
    for i in range(n):
        a_cnt += arr[i].count(1)
        v_cnt += v[i].count(-1)
    if a_cnt == v_cnt:
        return max_val
    else:
        return 10**6
    

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[-1]*n for _ in range(n)]
min_t = 10**6
bk(0, 0, 0, [])
print(min_t if min_t != 10**6 else -1)

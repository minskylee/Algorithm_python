# https://www.acmicpc.net/problem/17837
# 새로운 게임 2


def move(chess):
    cr, cc, d = obj[chess]
    nr, nc = cr+dr[d], cc+dc[d]

    if not (0 <= nr < n and 0 <= nc < n) or arr[nr][nc] == 2:
        if d <= 1:
            nd = (d+1)%2
        else:
            nd = 2 + (d+1)%2
        obj[chess][2] = nd
        nr, nc = cr+dr[nd], cc+dc[nd]
        if not (0 <= nr < n and 0 <= nc < n) or arr[nr][nc] == 2:
            return 0
    
    obj_set = []
    for i in range(len(v[cr][cc])):
        if v[cr][cc][i] == chess:
            obj_set.extend(v[cr][cc][i:])
            v[cr][cc] = v[cr][cc][:i]
            break
    
    if arr[nr][nc] == 1:
        obj_set = obj_set[::-1]
    
    for i in obj_set:
        v[nr][nc].append(i)
        obj[i][:2] = [nr, nc]
    
    if len(v[nr][nc]) >= 4:
        return 1
    return 0


def check_chess():
    cnt = 1
    while cnt <= 1000:
        for i in range(1, m+1):
            flg = move(i)
            if flg:
                return cnt
        cnt += 1
    return -1


dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[[] for _ in range(n)] for _ in range(n)]
obj = [[0, 0, 0]]
for i in range(1, m+1):
    r, c, d = list(map(int, input().split()))
    obj.append([r-1, c-1, d-1])
    v[r-1][c-1].append(i)

print(check_chess())

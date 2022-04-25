# https://www.acmicpc.net/problem/16234
# 인구 이동


from collections import deque


def bfs(r, c, region):
    queue = deque()
    queue.append((r, c))
    v[r][c] = region
    sum_val, cnt_val = arr[r][c], 1
    flg = 0
    while queue:
        s = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = s[0]+d[0], s[1]+d[1]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc]:
                if L <= abs(arr[nr][nc]-arr[s[0]][s[1]]) <= R:
                    v[nr][nc] = region
                    flg = 1
                    sum_val += arr[nr][nc]
                    cnt_val += 1
                    queue.append((nr, nc))
    c_people = sum_val//cnt_val
    if not flg and arr[r][c] == c_people:
        return 0
    for i in range(n):
        for j in range(n):
            if v[i][j] == region:
                arr[i][j] = c_people
    return 1


n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
day_cnt = 0
while day_cnt <= 2000:
    end_flg = 0
    v = [[0]*n for _ in range(n)]
    region = 1
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                end_flg += bfs(i, j, region)
                region += 1
    if not end_flg:
        break
    day_cnt += 1
print(day_cnt)

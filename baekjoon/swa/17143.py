# https://www.acmicpc.net/problem/17143
# 낚시왕



R, C, M = map(int, input().split())
arr = [[[0, 0] for _ in range(C)] for _ in range(R)]
dr, dc = (-1, 1, 0, 0), (0, 0, 1, -1)
shark = [[0]*4 for _ in range(M)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[i] = [r-1, c-1, s, d-1]
    arr[r-1][c-1] = [i, z]
fish = 0
for fishking in range(C):
    for deep in range(R):
        if arr[deep][fishking] != [0, 0]:
            fish += arr[deep][fishking][1]
            shark[arr[deep][fishking][0]] = [-1, -1, -1, -1]
            arr[deep][fishking] = [0, 0]
            break
    n_arr = [[[0, 0] for _ in range(C)] for _ in range(R)]
    for i in range(M):
        if shark[i] != [-1, -1, -1, -1]:
            r, c, s ,d = shark[i]
            if d < 2:
                s %= (R-1)*2
            else:
                s %= (C-1)*2
            nr, nc = r, c
            for _ in range(s):
                nr, nc = nr+dr[d], nc+dc[d]
                if not (0 <= nr < R and  0 <= nc < C):
                    d = (d//2)*2+(d+1)%2
                    nr, nc = nr+dr[d]*2, nc+dc[d]*2
            shark[i] = [nr, nc, s, d]


            if n_arr[nr][nc] != [0, 0]:
                if n_arr[nr][nc][1] > arr[r][c][1]:
                    shark[i] = [-1, -1, -1, -1]
                else:
                    shark[n_arr[nr][nc][0]] = [-1, -1, -1, -1]
                    n_arr[nr][nc] = arr[r][c]
            else:
                n_arr[nr][nc] = arr[r][c]
    arr = n_arr
print(fish)

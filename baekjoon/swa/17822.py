# https://www.acmicpc.net/problem/17822
# 원판 돌리기


from copy import deepcopy


def solve():
    n_arr = deepcopy(arr)
    flg = cnt = sum_val = 0
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                continue
            for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = i+d[0], j+d[1]
                if 0 <= nr < n and -1 <= nc < m:
                    if arr[nr][nc] == arr[i][j]:
                        n_arr[nr][nc] = 0
                        n_arr[i][j] = 0
                        flg = 1
            if n_arr[i][j] != 0:
                cnt += 1
                sum_val += n_arr[i][j]
    if not flg and cnt:
        avg_num = sum_val / cnt
        for i in range(n):
            for j in range(m):
                if not n_arr[i][j]:
                    continue
                if n_arr[i][j] < avg_num:
                    n_arr[i][j] += 1
                elif n_arr[i][j] > avg_num:
                    n_arr[i][j] -= 1
    return n_arr


n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rot = [list(map(int, input().split())) for _ in range(t)]
for cmd in rot:
    x, d, k = cmd
    rot_x = [x-1 for x in range(x, n+1, x)]
    k = (k%m)
    for xx in rot_x:
        for _ in range(k):
            if d == 0:
                arr[xx].insert(0, arr[xx].pop())
            else:
                arr[xx].append(arr[xx].pop(0))
    arr = solve()
print(sum(map(sum, arr)))

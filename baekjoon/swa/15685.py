# https://www.acmicpc.net/problem/15685
# 드래곤 커브


'''
# 좌표를 담아놓은 배열을 하나 만듬
# 그 배열을 복사해 시계방향으로 90도 돌리고, 끝배열에 붙임
'''

n = int(input())
arr_map = [[0]*101 for _ in range(101)]
dr, dc = (0, -1, 0, 1), (1, 0, -1, 0)
arr = []
c_cnt = [0]*n
dir_arr = [[] for _ in range(n)]
for i in range(n):
    x, y, d, g = map(int, input().split())
    arr.append([(y, x)])
    arr_map[y][x] = 1
    dir_arr[i].append(d)
    c_cnt[i] = g
idx = 0
while idx < n:
    if not c_cnt[idx]:
        for d in dir_arr[idx]:
            ny, nx = arr[idx][-1][0]+dr[d], arr[idx][-1][1]+dc[d]
            arr[idx].append((ny, nx))
            arr_map[ny][nx] = 1
        idx += 1
    else:
        c_cnt[idx] -= 1
        for d in dir_arr[idx][::-1]:
            dir_arr[idx].append((d+1)%4)
ans = 0
for i in range(100):
    for j in range(100):
        if arr_map[i][j] == 1 and arr_map[i+1][j] == 1 and arr_map[i][j+1] == 1 and arr_map[i+1][j+1] == 1:
            ans += 1
print(ans)

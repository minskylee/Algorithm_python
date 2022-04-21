# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

'''
# Red구슬과 Blue구슬의 위치를 파악하고, 방문배열에 기록한다.
# 이 때, 방문여부는 4차원 배열로 2*2, 2*2 를 사용한다.
# 구슬을 굴릴 때, 벽이나 구멍이 나오기 전까지 이동한다.
# 파란구슬이 구멍이라면 무시한다.
# 구슬을 굴리고, 빨강, 파랑 구슬의 위치가 같다면, 더 먼 거리를 이동한 구슬을 한칸 뒤로 돌린다.
# 빨강구슬이 구멍이라면 현재 굴린 횟수를 리턴한다.
# 10번 이상 굴리면 종료한다.
# 이동할 곳이 없으면 종료한다.
'''


import sys
from collections import deque
input = sys.stdin.readline


def bfs(q):
    while q:
        rr, rc, br, bc, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrr, nrc, r_cnt = move(rr, rc, dr[i], dc[i], 0)
            nbr, nbc, b_cnt = move(br, bc, dr[i], dc[i], 0)
            if arr[nbr][nbc] == 'O':
                continue
            elif arr[nrr][nrc] == 'O':
                return d
            if nrr == nbr and nrc == nbc:
                if r_cnt > b_cnt:
                    nrr, nrc = nrr-dr[i], nrc-dc[i]
                else:
                    nbr, nbc = nbr-dr[i], nbc-dc[i]
            if not v[nrr][nrc][nbr][nbc]:
                v[nrr][nrc][nbr][nbc] = 1
                q.append((nrr, nrc, nbr, nbc, d+1))
    return -1
            

def move(r, c, _dr, _dc, cnt):
    while arr[r+_dr][c+_dc] != '#' and arr[r][c] != 'O':
        r += _dr
        c += _dc
        cnt += 1
    return r, c, cnt


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
v = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
q = deque()

crr = crc = cbr = cbc = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            crr, crc = i, j
        elif arr[i][j] == 'B':
            cbr, cbc = i, j
v[crr][crc][cbr][cbc] = 1
q.append((crr, crc, cbr, cbc, 1))
print(bfs(q))

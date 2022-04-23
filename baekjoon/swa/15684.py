# https://www.acmicpc.net/problem/15684
# 사다리 조작

'''
# n, m 개의 가로선과 세로선이 있음.
# 세로선 마다 가로선을 놓을 수 있는 위치의 갯수는 H가 있음
# 세로선을 2배의 크기로 배열을 만듬
# 바로 옆 빈공간에는 가로선이 같이 있을 수 없음
'''
import sys
input = sys.stdin.readline


def bk(cnt, cr, cc):
    global ans
    if cnt > 3 and ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    for i in range(cr, h):
        if i == cr:
            k = cc
        else:
            k = 0
        for j in range(k, n-1):
            if not arr[i][j] and not arr[i][j+1]:
                if j > 0 and arr[i][j-1]:
                    continue
                arr[i][j] = 1
                bk(cnt+1, i, j+2)
                arr[i][j] = 0


def check():
    for start in range(n):
        line = start
        for j in range(h):
            if arr[j][line]:
                line += 1
            elif line > 0 and arr[j][line-1]:
                line -= 1
        if line != start:
            return False
    return True


n, m, h = map(int, input().split())
arr = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
ans = 4
if m == 0:
    print(0)
else:    
    bk(0, 0, 0)
    print(ans if ans < 4 else -1)

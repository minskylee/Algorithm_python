# https://www.acmicpc.net/problem/2580
# 스도쿠


import sys
input = sys.stdin.readline

def sudoku(idx):
    if idx == len_zero:
        for row in arr:
            print(*row)
        sys.exit(0)
    r, c = z_arr[idx]
    num_arr = is_num(r, c)
    for i in range(1, 10):
        # 들어갈 수 있는 수를 모두 대입해 봄
        if i in num_arr:
            arr[r][c] = i
            sudoku(idx+1)
            arr[r][c] = 0
    

# 들어갈 수 있는 수 판단
def is_num(r, c):
    num = [x for x in range(10)]
    for k in range(9):
        if arr[r][k]:
            num[arr[r][k]] = 0
        if arr[k][c]:
            num[arr[k][c]] = 0
    nr = r//3*3
    nc = c//3*3
    for a in range(3):
        for b in range(3):
            if arr[nr+a][nc+b]:
                num[arr[nr+a][nc+b]] = 0
    return num

arr = [list(map(int, input().split())) for _ in range(9)]
# 0 위치 찾기
z_arr = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
len_zero = len(z_arr)
sudoku(0)
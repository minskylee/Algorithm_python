# https://www.acmicpc.net/problem/5373
# 큐빙


def move(c_area):
    if c_area == 'U':
        U, L, F, R, B = up, left, front, right, back
    elif c_area == 'D':
        U, L, F, R, B = down, back, right, front, left
    elif c_area == 'F':
        U, L, F, R, B = front, up, left, down, right
    elif c_area == 'B':
        U, L, F, R, B = back, right, down, left, up
    elif c_area == 'L':
        U, L, F, R, B = left, front, up, back, down
    else:    # c_area == 'R'
        U, L, F, R, B = right, down, back, up, front
    # 윗면
    U[0][2], U[1][2], U[2][2], U[2][1], U[2][0], U[1][0], U[0][0], U[0][1] = U[0][0], U[0][1], U[0][2], U[1][2], U[2][2], U[2][1], U[2][0], U[1][0]
    # 옆면
    L[2][2], L[2][1], L[2][0], F[2][0], F[1][0], F[0][0], R[0][2], R[1][2], R[2][2], B[0][0], B[0][1], B[0][2] = F[2][0], F[1][0], F[0][0], R[0][2], R[1][2], R[2][2], B[0][0], B[0][1], B[0][2], L[2][2], L[2][1], L[2][0]


T = int(input())
for _ in range(T):
    n = int(input())
    rot = list(input().split())
    up = [['w' for _ in range(3)] for _ in range(3)]
    down = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]
    for c_area, c_dir in rot:
        move(c_area)
        if c_dir == '-':
            move(c_area)
            move(c_area)

    for i in range(3):
        print(''.join(up[i]))

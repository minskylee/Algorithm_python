# https://www.acmicpc.net/problem/16235
# 나무 재테크


n, m, k = map(int, input().split())
add_yy = [list(map(int, input().split())) for _ in range(n)]
dr, dc = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)
yy = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
for _ in range(k):
    tree_die = []
    tree_baby = []
    # spring
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                for t in range(len(tree[i][j])):
                    yy[i][j] -= tree[i][j][t]
                    if yy[i][j] >= 0:
                        tree[i][j][t] += 1
                        if not tree[i][j][t]%5:
                            tree_baby.append((i, j))
                    else:   # tree die
                        yy[i][j] += tree[i][j][t]
                        tree_die.append((i, j, t))
                        break
    # summer
    for yi, yj, yt in tree_die:
        for _ in range(len(tree[yi][yj])-yt):
            yy[yi][yj] += (tree[yi][yj].pop()//2)
    # fall
    for i, j in tree_baby:
        for d in range(8):
            nr, nc = i+dr[d], j+dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                tree[nr][nc].append(1)
    # winter
    for i in range(n):
        for j in range(n):
            yy[i][j] += add_yy[i][j]
tree_cnt = 0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            tree_cnt += len(tree[i][j])
print(tree_cnt)

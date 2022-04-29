# https://www.acmicpc.net/problem/20061
# 모노미노도미노 2


def move_blue(t, x):
    y = 1
    if t == 1 or t == 2:
        while True:
            if y + 1 > 5 or blue[x][y+1]:
                blue[x][y] = 1
                if t == 2:
                    blue[x][y-1] = 1
                break
            y += 1
    else:   # t == 3
        while True:
            if y + 1 > 5 or blue[x][y+1] or blue[x+1][y+1]:
                blue[x][y] = blue[x+1][y] = 1
                break
            y += 1 
    
    check_blue()

    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                remove_blue(5)
                break

   
def move_green(t, y):
    x = 1
    if t == 1 or t == 3:
        while True:
            if x + 1 > 5 or green[x+1][y]:
                green[x][y] = 1
                if t == 3:
                    green[x-1][y] = 1
                break
            x += 1
    else:
        while True:
            if x + 1 > 5 or green[x+1][y] or green[x+1][y+1]:
                green[x][y], green[x][y+1] = 1, 1
                break
            x += 1
    check_green()
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                remove_green(5)
                break


def check_blue():
    global score
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt == 4:
            remove_blue(j)
            score += 1

def check_green():
    global score
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1

        if cnt == 4:
            remove_green(i)
            score += 1


def remove_blue(idx):
    for j in range(idx, 0, -1):
        for i in range(4):
            blue[i][j] = blue[i][j-1]
    for i in range(4):
        blue[i][0] = 0


def remove_green(idx):
    for i in range(idx, 0, -1):
        for j in range(4):
            green[i][j] = green[i-1][j]
    for j in range(4):
        green[0][j] = 0


n = int(input())

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]

score = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    move_blue(t, x)
    move_green(t, y)

print(score)
print(sum(map(sum, blue)) + sum(map(sum, green)))

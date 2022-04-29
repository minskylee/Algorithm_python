# https://www.acmicpc.net/problem/17825
# 주사위 윷놀이


from copy import deepcopy


def bk(n, score, horse):
    global max_score
    if n == 10:
        max_score = max(max_score, score)
        return
    
    for h in range(4):
        if horse[h][0] == -1:
            continue
        tmp = deepcopy(horse)
        tmp[h][0] += dice[n]

        if tmp[h][1] == 0:
            if tmp[h][0] == 5:
                tmp[h][1] = 1
                tmp[h][0] = 0
            elif tmp[h][0] == 10:
                tmp[h][1] = 2
                tmp[h][0] = 0
            elif tmp[h][0] == 15:
                tmp[h][1] = 3
                tmp[h][0] = 0
        
        if tmp[h][0] >= len(road[tmp[h][1]]):
            tmp[h][0] = -1
            bk(n+1, score, tmp)
        else:
            flg = False
            visit = road[tmp[h][1]][tmp[h][0]]
            for v in range(4):
                if tmp[v][0] == -1:
                    continue
                if v != h and visit == road[tmp[v][1]][tmp[v][0]]:
                    if visit == 30:
                        if tmp[h] == [0, 3] and tmp[v] == [0, 3]:
                            flg = True
                            break
                        elif tmp[h] != [0, 3] and tmp[v] != [0, 3]:
                            flg = True
                            break
                    elif visit in [16, 22, 24, 26, 28]:
                        if tmp[h] == tmp[v]:
                            flg = True
                            break
                    else:
                        flg = True
                        break
            if flg:
                continue
            bk(n+1, score + road[tmp[h][1]][tmp[h][0]], tmp)

road = [
    [x*2 for x in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40],
]
dice = list(map(int, input().split()))
horse = [[0, 0] for _ in range(4)]
max_score = 0
bk(0, 0, horse)
print(max_score)

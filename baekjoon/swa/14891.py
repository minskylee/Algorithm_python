# https://www.acmicpc.net/problem/14891
# 톱니바퀴


'''
# 어떤 톱니바퀴가 돌아갔을 때, 다른 톱니바퀴와 접점이 있는 idx를 확인한다.
# 접점이 있는 위치는 왼쪽에 있는 톱니의 경우 (6, 2) 오른쪽의 경우 (2, 6)
# 만약 다른 인덱스라면 주어진 방향에 따라 회전함
# 회전은 -1 = G.append(G.pop(0)) or 1 = G.insert(0, G.pop())으로 넣음
'''


G = [list(map(int, input())) for _ in range(4)]
k = int(input())
rot = [list(map(int, input().split())) for _ in range(k)]
for move in rot:
    rot_gear = [0]*4
    c_gear = move[0]-1
    rot_gear[c_gear] = move[1]
    for n_gear in range(c_gear+1, 4):
        if G[c_gear][2] != G[n_gear][6]:
            rot_gear[n_gear] = -rot_gear[c_gear]
            c_gear = n_gear
        else:
            break
    c_gear = move[0]-1
    for n_gear in range(c_gear-1, -1, -1):
        if G[c_gear][6] != G[n_gear][2]:
            rot_gear[n_gear] = -rot_gear[c_gear]
            c_gear = n_gear
        else:
            break
    for idx in range(4):
        if rot_gear[idx] == -1:
            G[idx].append(G[idx].pop(0))
        elif rot_gear[idx] == 1:
            G[idx].insert(0, G[idx].pop())
ans = 0
for i in range(4):
    ans += G[i][0]*2**(i)
print(ans)

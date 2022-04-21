# https://www.acmicpc.net/problem/3190
# 뱀


'''
# 뱀의 처음위치는 (0, 0) 길이는 1 방향은 오른쪽
# 사과의 좌표에 도달하면, 길이가 1 늘어남
# 사과가 없으면 길이 유지, 계속 이동함
# 일정시간이 지난 후 방향이 변함
# 벽 또는 자기자신의 몸과 부딪히면 게임 끝
'''
from collections import deque

n = int(input())
k = int(input())
apple = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
l  = int(input())
s_dir = [tuple(input().split()) for _ in range(l)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
snake = deque()
s_head, d, ch_d_time= (0, 0), 0, 0
snake.append(s_head)
game_time = 0
while 0 <= s_head[0] < n and 0 <= s_head[1] < n:
    game_time += 1
    s_head = (s_head[0]+dr[d%4], s_head[1]+dc[d%4])
    if s_head in snake:
        break
    snake.append(s_head)
    # 사과 냠냠
    if s_head not in apple:
        snake.popleft()
    else:
        apple.remove(s_head)
    # 방향 변환 정보
    if ch_d_time < len(s_dir) and game_time == int(s_dir[ch_d_time][0]):
        if s_dir[ch_d_time][1] == 'D':
            d += 1
        else:
            d -= 1
        ch_d_time += 1
print(game_time)

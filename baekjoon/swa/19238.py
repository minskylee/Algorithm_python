# https://www.acmicpc.net/problem/19238
# 스타트 택시


from collections import deque


def find_people(start):
    q = deque()
    q.append(start)
    visited = [[0]*n for _ in range(n)]
    min_distance = 500
    taxi = []
    while q:
        s = q.popleft()
        if visited[s[0]][s[1]] > min_distance:
            break
        if s in people:
            min_distance = visited[s[0]][s[1]]
            taxi.append(s)
        else:
            for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = s[0]+d[0], s[1]+d[1]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = visited[s[0]][s[1]] + 1
                    q.append((nr, nc))
    if taxi:
        taxi.sort()
        return visited[taxi[0][0]][taxi[0][1]], taxi[0][0], taxi[0][1]
    else:
        return -1, -1, -1

def find_destinatnion(start, end):
    q = deque()
    q.append(start)
    visited = [[0]*n for _ in range(n)]
    while q:
        s = q.popleft()
        if s == end:
            break
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = s[0]+d[0], s[1]+d[1]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[s[0]][s[1]] + 1
                q.append((nr, nc))
    return visited[s[0]][s[1]], s[0], s[1]



n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
start = (r-1, c-1)
people, destination = [], []
for _ in range(m):
    pr, pc, dr, dc = map(int, input().split())
    people.append((pr-1, pc-1))
    destination.append((dr-1, dc-1))

for _ in range(m):
    distance, pr, pc = find_people(start)
    if distance == -1 or fuel - distance < 0:
        fuel = -1
        break
    fuel -= distance
    idx = people.index((pr, pc))
    people[idx] = (-1, -1)

    distance2, dr, dc = find_destinatnion((pr, pc), destination[idx])
    if (dr, dc) != destination[idx] or fuel - distance2 < 0:
        fuel = -1
        break
    fuel += distance2
    start = (dr, dc)


print(fuel)

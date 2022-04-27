# https://www.acmicpc.net/problem/17779
# 게리맨더링 2


def solve(x, y, d1, d2):
    election = [[0]*(n+1) for _ in range(n+1)]
    election[x][y] = 5
    for i in range(1, d1+1):
        election[x+i][y-i] = 5
    for i in range(1, d2+1):
        election[x+i][y+i] = 5
    for i in range(1, d2+1):
        election[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        election[x+d2+i][y+d2-i] = 5
    
    people = [0]*5
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if election[r][c] == 5:
                break
            else:
                people[0] += arr[r][c]
    
    for r in range(1, x+d2+1):
        for c in range(n, y, -1):
            if election[r][c] == 5:
                break
            else:
                people[1] += arr[r][c]
    
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if election[r][c] == 5:
                break
            else:
                people[2] += arr[r][c]
    
    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1, -1):
            if election[r][c] == 5:
                break
            else:
                people[3] += arr[r][c]

    people[4] = total - sum(people)
    return max(people) - min(people)

n = int(input())
arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
total = sum(map(sum, arr))

ans = 10**6
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x+d1+d2 > n:
                    continue
                if y-d1 < 1:
                    continue
                if y+d2 > n:
                    continue

                ans = min(ans, solve(x, y, d1, d2))
print(ans)


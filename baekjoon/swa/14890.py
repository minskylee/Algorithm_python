# https://www.acmicpc.net/problem/14890
# 경사로


'''
# 지나갈 수 있는 길의 갯수를 판별
# 높이 차이가 2라면 조건 불만족
# 높이가 1 차이나는 경사로의 작은부분이 L길이만큼의 여유가있다면 조건 만족
# L길이의 여유가 없다면 조건 불만족
'''
    

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    # 가로축
    hight_road = arr[i][0]
    cnt_road = 0
    for j in range(n):
        if hight_road == arr[i][j]:
            cnt_road += 1
        elif hight_road == arr[i][j]-1 and cnt_road >= l:
            cnt_road = 1
            hight_road = arr[i][j]
        elif hight_road == arr[i][j]+1 and cnt_road >= 0:
            cnt_road = -l+1
            hight_road = arr[i][j]
        else:
            break
    else:
        if cnt_road >= 0:
            ans += 1

for j in range(n):
    # 세로축
    hight_road = arr[0][j]
    cnt_road = 0
    for i in range(n):
        if hight_road == arr[i][j]:
            cnt_road += 1
        elif hight_road == arr[i][j]-1 and cnt_road >= l:
            cnt_road = 1
            hight_road = arr[i][j]
        elif hight_road == arr[i][j]+1 and cnt_road >= 0:
            cnt_road = -l+1
            hight_road = arr[i][j]
        else:
            break
    else:
        if cnt_road >= 0:
            ans += 1

print(ans)

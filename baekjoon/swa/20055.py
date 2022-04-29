# https://www.acmicpc.net/problem/20055
# 컨베이어 벨트 위의 로봇


n, k = map(int, input().split())
arr = list(map(int, input().split()))
belt = [0]*n
cnt = 0

while True:
    arr.insert(0, arr.pop())
    belt.insert(0, belt.pop())
    belt[-1] = 0
    if sum(belt):
        for i in range(n-2, -1, -1):
            if belt[i+1] == 0 and belt[i] == 1 and arr[i+1] > 0:
                belt[i+1], belt[i] = belt[i], belt[i+1]
                arr[i+1] -= 1
        belt[-1] = 0
    if arr[0] > 0 and not belt[0]:
        belt[0] = 1
        arr[0] -= 1
    cnt += 1
    if arr.count(0) >= k:
        break
print(cnt)

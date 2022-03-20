# https://www.acmicpc.net/problem/2156
# 포도주 시식


N = int(input())
arr = [int(input()) for _ in range(N)]
max_arr = [0]*N
if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0]+arr[1])
else:
    max_arr[0] = arr[0]
    max_arr[1] = arr[1] + arr[0]
    max_arr[2] = max(arr[2]+arr[1], arr[2]+arr[0], max_arr[1])
    for i in range(3, N):
        max_arr[i] = max(arr[i] + arr[i-1] + max_arr[i-3], arr[i] + max_arr[i-2], max_arr[i-1])
    print(max(max_arr))

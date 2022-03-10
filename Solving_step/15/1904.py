# https://www.acmicpc.net/problem/1904
# 01타일

N = int(input())
arr = [0]*1000000
arr[0] = 1
arr[1] = 2
for i in range(2, N):
    arr[i] = (arr[i-1] + arr[i-2])% 15746
print(arr[N-1])

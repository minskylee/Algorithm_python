# https://www.acmicpc.net/problem/1912
# 연속합


N = int(input())
arr = list(map(int, input().split()))
sum_arr = [0]*N
sum_arr[0] = arr[0]
for i in range(1, N):
    sum_arr[i] = max(sum_arr[i-1]+arr[i], arr[i])
print(max(sum_arr))
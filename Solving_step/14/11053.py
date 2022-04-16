# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열


N = int(input())
arr = list(map(int, input().split()))
len_arr = [1]*N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            len_arr[i] = max(len_arr[i], len_arr[j]+1)
print(max(len_arr))

# https://www.acmicpc.net/problem/1003
# 피보나치 함수


N = int(input())
f0_arr = [0]*41
f0_arr[0] = 1
f0_arr[1] = 0
f1_arr = [0]*41
f1_arr[0] = 0
f1_arr[1] = 1
for i in range(2, 41):
    f0_arr[i] = f0_arr[i-1]+f0_arr[i-2]
    f1_arr[i] = f1_arr[i-1]+f1_arr[i-2]
for _ in range(N):
    idx = int(input())
    print(f0_arr[idx], f1_arr[idx])
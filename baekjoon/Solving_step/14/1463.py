# https://www.acmicpc.net/problem/1463
# 1로 만들기


N = int(input())
# 1. if X % 3 == 0; X//3
# 2. if X % 2 == 0; X//2
# 3. if X -= 1
arr = [0]*(10**6+1)
arr[1] = 0
arr[2] = 1
arr[3] = 1
for i in range(4, 10**6+1):
    a = b = c = 1000
    if i % 3 == 0:
        a = arr[i//3] + 1
    if i % 2 == 0:
        b = arr[i//2] + 1
    c = arr[i-1] + 1
    arr[i] = min(a, b, c)
print(arr[N])
# https://www.acmicpc.net/problem/9461
# 파도반 수열


tri_list = [1, 1, 1]
for i in range(3, 101):
    tri_list.append(tri_list[i-3]+tri_list[i-2])


T = int(input())

for _ in range(T):
    N = int(input())
    print(tri_list[N-1])
    
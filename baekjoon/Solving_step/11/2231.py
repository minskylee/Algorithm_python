# https://www.acmicpc.net/problem/2231
# 분해합

N = int(input())

make_list = []
for i in range(1, N+1):
    sum_val = i
    for s in str(i):
        sum_val += int(s)
    make_list.append(sum_val)

if N in make_list:
    print(make_list.index(N)+1)
else:
    print(0)
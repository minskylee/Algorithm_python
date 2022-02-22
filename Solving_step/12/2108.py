# https://www.acmicpc.net/problem/2108
# 통계학


import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
n_arr = []
for _ in range(N):
    n_arr.append(int(input()))
n_arr.sort()

tmp = Counter(n_arr).most_common(2)
if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        mod = tmp[1][0]
    else:
        mod = tmp[0][0]
else:
    mod = tmp[0][0]
print(tmp)
print(round(sum(n_arr)/N))
print(n_arr[(N-1)//2])
print(mod)
print(n_arr[-1] - n_arr[0])

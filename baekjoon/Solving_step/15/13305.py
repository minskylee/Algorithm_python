# https://www.acmicpc.net/problem/13305
# 주유소


N = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

cost, s_val = p[0], 0
for i in range(N-1):
    if cost > p[i]:
        cost = p[i]
    s_val += cost*d[i]
print(s_val)
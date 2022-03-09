# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수


a, b = map(int, input().split())

a_set = set()
b_set = set()
for i in range(1,a+1):
    if a%i == 0:
        a_set.add(i)

for i in range(1,b+1):
    if b%i == 0:
        b_set.add(i)

max_val = max(a_set & b_set)
print(max_val)
print(int(max_val * a/max_val * b/max_val))
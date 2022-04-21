# https://www.acmicpc.net/problem/2751
# 수 정렬하기2


import sys
n = int(input())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    sys.stdout.write(str(i)+'\n')
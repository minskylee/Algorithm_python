import sys

N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1, A+B))
import sys

input = int(sys.stdin.readline())

for i in range(input):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
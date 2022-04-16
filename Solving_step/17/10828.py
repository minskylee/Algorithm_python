# https://www.acmicpc.net/problem/10828
# 스택

import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
N = int(input())
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

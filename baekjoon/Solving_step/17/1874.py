# https://www.acmicpc.net/problem/1874
# 스택 수열


N = int(input())
arr = [x for x in range(N, 0, -1)]
stack, result = [], []
ans = ''
for _ in range(N):
    n = int(input())
    while arr and arr[-1] <= n:
        stack.append(arr.pop())
        result.append('+')
    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else:
        ans = 'NO'
if ans:
    print(ans)
else:
    for c in result:
        print(c)
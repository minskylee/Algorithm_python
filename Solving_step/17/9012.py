# https://www.acmicpc.net/problem/9012
# 괄호

T = int(input())
for _ in range(T):
    arr = []
    for i in input():
        if i == '(':
            arr.append(i)
        else:
            if arr:
                arr.pop()
            else:
                print('NO')
                break
    else:
        if arr:
            print('NO')
        else:
            print('YES')

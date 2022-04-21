# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

while True:
    s_arr = input()
    if s_arr == '.':
        break
    stack = []
    ans = 'no'
    for c in s_arr:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                break
        elif c == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
            else:
                break
    else:
        if not stack:
            ans = 'yes'
    print(ans)

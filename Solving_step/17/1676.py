# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)


num = str(fac(int(input())))
cnt = 0
for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        print(cnt)
        break
    cnt += 1
else:
    print(0)

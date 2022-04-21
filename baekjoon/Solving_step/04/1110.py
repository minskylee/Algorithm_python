import sys

N = input()

if len(N) == 1:
        N = ("0"+ N)

first = N
cnt = 0

while True:
    N = N[1]+ str((int(N[0])+int(N[1])))[-1]
    cnt += 1
    if first == N:
        print(cnt)
        break
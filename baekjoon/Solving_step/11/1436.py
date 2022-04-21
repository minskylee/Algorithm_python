# https://www.acmicpc.net/problem/1436
# 영화감독 숌

N = int(input())

title_num = 666
cnt = 1
while True:
    if '666' in str(title_num):
        if cnt == N:
            print(title_num)
            break
        cnt += 1
    title_num += 1

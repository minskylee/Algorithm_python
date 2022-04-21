# https://www.acmicpc.net/problem/15652
# N과 M(4)


def f(idx):
    if idx == M:
        print(*select)
        return
    for i in range(N):
        if idx != 0 and select[idx-1] > arr[i]:
                continue
        select[idx] = arr[i]
        f(idx+1)

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
select = [0] * M
f(0)
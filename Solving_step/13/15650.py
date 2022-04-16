# https://www.acmicpc.net/problem/15650
# N과 M(2)


def f(idx):
    if idx == M:
        print(*select)
        return
    for i in range(N):
        if not used[i]:
            if idx != 0 and select[idx-1] > i:
                continue
            select[idx] = arr[i]
            used[i] = 1
            f(idx+1)
            used[i] = 0

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
select = [0] * M
used = [0] * N
f(0)
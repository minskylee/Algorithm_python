N = int(input())
N_num = list(map(int, input().split()))

N_max = N_min = N_num[0]
if N == len(N_num):
    for i in N_num:
        if N_max < i:
            N_max = i
        if N_min > i:
            N_min = i
print(N_min, N_max)
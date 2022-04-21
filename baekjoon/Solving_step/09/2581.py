def is_pri_num(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

M = int(input())
N = int(input())

pri_list = list(filter(is_pri_num, range(M, N+1)))
if pri_list:
    print(sum(pri_list))
    print(pri_list[0])
else:
    print(-1)
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    for f in range(k+1):
        if f == 0:
            neigh_num = [i for i in range(1, n+1)]
        else:
            neigh_num = [sum(neigh_num[:i]) for i in range(1, n+1)]
    print(neigh_num[-1])
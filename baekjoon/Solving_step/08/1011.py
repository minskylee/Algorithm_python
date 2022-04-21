from math import ceil


T = int(input())

for _ in range(T):
    x, y = map(int,input().split())
    x, y = 0, y-x

    max_loc = y//2
    # n(2a+d*(n-1))/2 # a, d = 1일 떄 n값
    # n(n+1)/2 < max_loc
    # 0.5(n**2 + n - 2*max_loc) < 0
    a, b, c = 1, 1, -2*max_loc
    n_u = ceil((-b + (b**b - 4*a*c)**0.5) / (2*a))
    max_loc = n_u*(n_u+1)/2

    # 1 에서 y - max_loc 까지 n_d
    # n(2*max_loc + n - 1)/2
    # 0.5(n**2 + n) < y - max_loc
    # 0.5(n**2 + n - 2*(y - max_loc)) < 0
    a, b, c = 1, 1, - 2*(y - max_loc)
    n_d = (-b + (b**b - 4*a*c)**0.5) / (2*a)
    print(ceil(n_u + n_d))






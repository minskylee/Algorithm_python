def star(n):

    if n <= 3:
        star_space[0][:3] = star_space[2][:3] = ['*', '*', '*']
        star_space[1][:3] = ['*', ' ', '*']
        return
    
    pre_n = n//3
    star(n//3)

    for i in range(3):
        for j in range(3):
            if i == 1 and j ==1:
                continue
            for star_pattern in range(i*pre_n, (i+1)*pre_n):
                star_space[star_pattern][j*pre_n:(j+1)*pre_n] = star_space[star_pattern-i*pre_n][:pre_n]


N = int(input())

star_space = [[' ' for _ in range(N)] for _ in range(N)]

star(N)

for s_list in star_space:
    print(*s_list, sep='')
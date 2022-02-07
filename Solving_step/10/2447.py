from math import log

def star(space, n):
    star_pattern = int(log(n, 3))

    if star_pattern == 1:
        star_space[0][:3] = star_space[2][:3] = [1, 1, 1]
        star_space[1][:3] = [1, 0, 1]
        return
    
    star(space, n//3)
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j ==1:
                pass
            star_space[][] = star_space[][]



N = int(input())

star_space = [[0 for _ in range(N)] for _ in range(N)]

star(star_space, N)
print(star_space)

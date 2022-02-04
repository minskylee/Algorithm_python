def star(n):
    if n < 1:
        return
    elif n == 1:
        print('***'+'\n' + '* *'+'\n' + '***'+'\n')
        return
    star_1 = ('***'*(n//3)+'\n' + '* *'*(n//3)+'\n' + '***'*(n//3)+'\n')
    
    
    return star(n-3)

N = int(input())

print(star(N))


# star_base = ('***'+'\n' + '* *'+'\n' + '***'+'\n')
# star_space = ('   '+'\n' + '   '+'\n' + '   '+'\n')
# star_1 = ('***'*(n//3)+'\n' + '* *'*(n//3)+'\n' + '***'*(n//3)+'\n')
# star_2 = ('***   ***'*(n//9)+'\n' + '* *   * *'*(n//9)+'\n' + '***   ***'*(n//9)+'\n')
# print(star_1 + star_2 + star_1)
# 1, 3, 9, 27, 81 ... 3**8

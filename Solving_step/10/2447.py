def star(n):
    star_base = ('***'+'\n' + '* *'+'\n' + '***'+'\n')
    star_space = ('   '+'\n' + '   '+'\n' + '   '+'\n')
    star_1 = ('***'*(n//3)+'\n' + '* *'*(n//3)+'\n' + '***'*(n//3)+'\n')
    star_2 = ('***   ***'*(n//9)+'\n' + '* *   * *'*(n//9)+'\n' + '***   ***'*(n//9)+'\n')
    print(star_1 + star_2 + star_1)
N = int(input())

print(star(N))
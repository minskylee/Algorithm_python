while True:
    tri_abc = list(map(int, input().split()))

    max_c = max(tri_abc)
    tri_abc.pop(tri_abc.index(max_c))
    
    if tri_abc == [0, 0] and max_c == 0:
        break
    print('right' if tri_abc[0]**2 + tri_abc[1]**2 == max_c**2 else 'wrong')

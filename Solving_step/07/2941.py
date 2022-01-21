cro_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cro_alph_input = input()

cro_cnt = 0
for i, c in enumerate(cro_alph_input):
    cro_cnt += 1
    if c == '-':
        cro_cnt -= 1
    elif c == '=':
        if cro_alph_input[i-1] == 'z':
            if cro_alph_input[i-2] == 'd':
                cro_cnt -= 2
            else:
                cro_cnt -= 1
        else:
            cro_cnt -= 1
    elif c == 'j':
        if cro_alph_input[i-1] == 'l' or cro_alph_input[i-1] == 'n':
            cro_cnt -= 1
print(cro_cnt)      
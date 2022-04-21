N_multi = 1
for i in range(3):
    N = int(input())
    N_multi *= N

arr_N_multi = [0 for i in range(10)]
for s in str(N_multi):
    arr_N_multi[int(s)] += 1
print(*arr_N_multi, sep='\n')
N = []
for i in range(9):
    N.append(int(input()))
print(max(N), N.index(max(N))+1, sep='\n')
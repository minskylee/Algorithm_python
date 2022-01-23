from math import ceil

N = list(map(int, input().split()))
print(ceil((N[2] - N[1])/(N[0] - N[1])))
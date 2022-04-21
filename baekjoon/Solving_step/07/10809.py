alpa = map(ord, input())

alphabet = [-1 for i in range(26)]
alpa_loc = 1
for c in alpa:
    if alphabet[c-97] == -1:
        alphabet[c-97] += alpa_loc
    alpa_loc += 1
print(*alphabet)

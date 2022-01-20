alpa = input().upper()

alpahbet = [0 for i in range(26)]
for a in alpa:
    alpahbet[ord(a)-65] += 1

max_val = 0
same_val = 0
max_idx = 0
for idx, a in enumerate(alpahbet):
    if max_val <= alpahbet[idx]:
        if max_val == alpahbet[idx]:
            same_val = alpahbet[idx]
        max_val = alpahbet[idx]
        max_idx = idx  

if same_val == max_val:    print('?')
else:   print(chr(65+max_idx))

A, B = map(int, input().split())

if B-45 < 0:
    if A == 0:
        A = 23
    else: 
        A -= 1
    
    B = B + 15
else:
    B = B-45

print(A,B)
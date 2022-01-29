def is_pri_num(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

while True:
    N = int(input())
    if N == 0:
        break
    
    cnt = 0
    for i in range(N + 1, 2*N + 1):
        if is_pri_num(i):
            cnt += 1
    print(cnt)

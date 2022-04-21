max_n = 123456*2
pri_list = [True for _ in range(max_n + 1)]
pri_list[1] = False
for i in range(2, int(max_n + 1)):
    if pri_list[i]:
        for j in range(2*i, max_n + 1, i):
            pri_list[j] = False
while True:
    N = int(input())
    if N == 0:
        break
    
    cnt = 0
    for i in range(N + 1, 2*N + 1):
        if pri_list[i]:
            cnt += 1
    print(cnt)

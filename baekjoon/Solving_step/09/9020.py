max_n = 10000
pri_list = [True for _ in range(max_n + 1)]
pri_list[1] = False
for i in range(2, int(max_n + 1)):
    if pri_list[i]:
        for j in range(2*i, max_n + 1, i):
            pri_list[j] = False

T = int(input())

for _ in range(T):
    n = int(input())
    
    for i in range(n//2, 1, -1):
        if pri_list[i] == True:
            if pri_list[n-i] ==True:
                print(i, n-i)
                break
# N Kg 배달 3 kg, 5 kg 봉지가 있음
# 더 적은 봉지를 가져감
N = int(input())

num = 0
for N_5 in range(0, N+1, 5):
    N_3, b = divmod((N - N_5), 3)
    if b == 0:
        num = N_5//5 + N_3
if num == 0:
    print(-1)
else:
    print(num)
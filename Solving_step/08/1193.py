# 대각선의 크기 1, 2, 3, ...
# 대각선의 크기는 (1+x)x / 2
# 짝수일 때 x/1, 홀수일 때 1/x으로 시작
# 입력이 N일 때 x(대각선의 위치)값은?
# N >= (1/2) * x**2 + (1/2) * x
# (1/2)*(x**2 + x - 2*N) <= 0
N = int(input())

x = (-(1/2) + ((1/2)**2 - 4*(1/2)*(N))**(1/2)) / (2*(1/2))
loc_foun = round(abs(x))
loc_foun_first = (1/2)*((loc_foun - 1)*((loc_foun - 1) + 1))
N_loc = int(N - loc_foun_first)
if loc_foun%2:
    
    print(f'{loc_foun - N_loc + 1}/{N_loc}')
else:
    print(f'{N_loc}/{loc_foun - N_loc + 1}')
num_list = list(map(int, input().split()))

sum_num = 0
for i in num_list:
    sum_num += i**2
print(sum_num%10)
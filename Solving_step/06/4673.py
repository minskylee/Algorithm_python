def d(n):
    self_num = n
    for i in range(len(str(n))):
        self_num += (n//10**i)%10
    return self_num

# 1. 1~10000까지 검토한다
# 2. self_number인 숫자를 뺴버린다.
# 1. time_error
# for self_number in range(1, 10001):
#     self_flag = 0
#     for n in range(1, 10001):
#         if self_number < n:
#             break
#         elif self_number == d(n):
#             self_flag = 1
#     if self_flag == 0:
#         print(self_number)

#2.
self_number = [i for i in range(1, 10001)]

non_self = set()
for n in range(1, 10001):
    non_num = d(n)
    if non_num <= 10000:
        non_self.add(non_num)

for i in non_self:
    self_number.remove(i)
print(*self_number, sep='\n')
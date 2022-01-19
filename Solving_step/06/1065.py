# 1. def_1
# def hansu_comp(n):
#     hansu_num = []
#     for i in str(n):
#         hansu_num.append(int(i))

#     hansu_flag = 0
#     if len(hansu_num) == 1:
#         hansu_flag = 1

#     compare_num = 0
#     for cur_num in range(1, len(hansu_num)):
#         if cur_num == 1:
#             compare_num = hansu_num[cur_num] - hansu_num[cur_num-1]
#             hansu_flag = 1
#         elif compare_num != hansu_num[cur_num] - hansu_num[cur_num-1]:
#             hansu_flag = 0
    
#     if hansu_flag == 1:
#         return True
#     else:
#         return False

# 2. def_2
def hansu_comp(n):
    if n < 100: return True
    elif (n//10)%10 *2 == (n//100) + (n%10):   return True
    else: return False

X = int(input())

cnt = 0
for i in range(1, X+1):
    cnt += hansu_comp(i)
print(cnt)
# https://www.acmicpc.net/problem/10814
# 나이순 정렬



def quick_sort(a):
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2][0]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in a:
        if int(num[0]) < int(pivot):
            lesser_arr.append(num)
        elif int(num[0]) > int(pivot):
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


N = int(input())
a_n_arr = []
for _ in range(N):
    a_n_arr.append(list(input().split()))

a_n_arr = quick_sort(a_n_arr)

for arr in a_n_arr:
    print(*arr)

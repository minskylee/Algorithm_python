# https://www.acmicpc.net/problem/1427
# 소트인사이드


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return  quick_sort(greater_arr) + equal_arr + quick_sort(lesser_arr)
    

a = list(map(int, input()))
a = quick_sort(a)
print(*a, sep='')
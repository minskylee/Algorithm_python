# https://www.acmicpc.net/problem/18870
# 좌표 압축


import sys
input = sys.stdin.readline


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    l_arr, m_arr, h_arr = [], [], []
    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif num > pivot:
            h_arr.append(num)
        else:
            if num not in m_arr:
                m_arr.append(num)
    return quick_sort(l_arr) + m_arr + quick_sort(h_arr)

N = int(input())
loc = list(map(int, input().split()))
sort_loc = quick_sort(loc)
dic = {sort_loc[i]: i for i in range(len(sort_loc))}
for a in loc:
    print(dic[a], end=' ')
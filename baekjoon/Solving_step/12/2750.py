# https://www.acmicpc.net/problem/2750
# 수 정렬하기

def insertion_sort(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i-1] > to_insert:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = to_insert

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

insertion_sort(lst)

for i in lst:
    print(i)
# https://www.acmicpc.net/problem/2798
# 블랙잭

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# N개중 3장을 뽑아 더한값이 M을 넘지 않는다
# 정렬을 한 뒤 M보다 작은 arr값에서 3장을 선택해 더한다
max_val = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
                sum_val = arr[i] + arr[j] + arr[k]
                if max_val < sum_val <= M:
                    max_val = sum_val
print(max_val)

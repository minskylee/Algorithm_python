# https://www.acmicpc.net/problem/1037
# 약수


N = int(input())
arr = list(map(int, input().split()))
print(max(arr)*min(arr))
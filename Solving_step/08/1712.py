# A: 고정비용 B: 한 대 가변비용 C: 한 대 노트북
cost = list(map(int, input().split()))

# n * cost[2] - n * cost[1] - cost[0] > 0
# n > cost[0] / (cost[2] - cost[1])
try:
    n = cost[0] // (cost[2] - cost[1]) + 1
    print(n if n > 0 else -1)
except(ZeroDivisionError):
    print(-1)

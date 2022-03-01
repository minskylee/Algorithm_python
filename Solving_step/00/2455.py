max_val = sum_val = 0
for _ in range(4):
    on, off = map(int, input().split())
    sum_val += (off - on)
    if max_val < sum_val:
        max_val = sum_val
print(max_val)
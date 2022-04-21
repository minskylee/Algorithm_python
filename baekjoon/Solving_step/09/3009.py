x = [0, 0, 0]
y = [0, 0, 0]
for i in range(3):
    x[i], y[i] = map(int, input().split())
for i in range(3):
    if x.count(x[i]) == 1:
        c_x = x[i]
    if y.count(y[i]) == 1:
        c_y = y[i]
print(c_x, c_y)
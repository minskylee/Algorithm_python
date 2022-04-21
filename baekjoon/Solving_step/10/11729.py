def move(n, start, end):
    print(start, end)

def h_top(n, start, end, wp):
    if n == 1:
        move(1, start, end)
        return
    h_top(n-1, start, wp, end)
    move(n, start, end)
    h_top(n-1, wp, end, start)

K = int(input())
print(2**K-1)
h_top(K, 1, 3, 2)

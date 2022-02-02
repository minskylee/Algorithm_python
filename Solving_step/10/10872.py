def fib(n):
    if n == 1 or n == 0:
        return 1
    return n*fib(n-1)

N = int(input())

print(fib(N))
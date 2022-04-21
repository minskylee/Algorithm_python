T = int(input())

for _ in range(T):
    r, s = input().split()
    for char_s in s:
        print(char_s*int(r), end='')
    print()

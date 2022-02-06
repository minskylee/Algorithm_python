a = b = 1
for i in range(2, int(input())):
    a, b = b, a + b
print(b)
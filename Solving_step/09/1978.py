N = int(input())
num = list(map(int, input().split()))

def is_pri_num(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

print(len(list(filter(is_pri_num, num))))
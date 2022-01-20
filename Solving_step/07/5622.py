min_time = 0
for c in input().upper():
    numb = (ord(c)-65)//3 + 2
    remain = (ord(c)-65)%3
    if numb < 8:
        min_time += numb + 1
    else:
        if remain == 0 or (numb == 10 and remain == 1):
            min_time += numb + 1 - 1
        else:
            min_time += numb + 1
print(min_time)
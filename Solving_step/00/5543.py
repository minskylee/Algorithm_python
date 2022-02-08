b_list = []
d_list = []
for i in range(5):
    price = int(input())
    if i < 3:
        b_list.append(price)
    else:
        d_list.append(price)

print(min(b_list)+min(d_list)-50)
# H층, W개의 방, N번째 손님

T = int(input())

for _ in range(T):
    hotel_room = list(map(int, input().split()))
    if hotel_room[2] % hotel_room[0] == 0:
        YY = hotel_room[2] * 100
        XX = hotel_room[2] // hotel_room[0]
    else:
        YY = (hotel_room[2] % hotel_room[0]) * 100
        XX = (hotel_room[2] // hotel_room[0]) + 1
    print(YY + XX)
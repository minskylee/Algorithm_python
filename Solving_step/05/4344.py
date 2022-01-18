test_case = int(input())

for i in range(test_case):
    score = list(map(int, input().split()))

    count = 0
    score_avg = sum(score[1:])/score[0]
    for num in range(score[0]):
        if score[num+1] > score_avg:
            count += 1
    print(f'{count / score[0] * 100:.3f}%')

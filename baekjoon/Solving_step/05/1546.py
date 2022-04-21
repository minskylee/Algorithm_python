N = int(input())
score = list(map(int, input().split()))

score_avg = 0
if N == len(score):
    for i in score:
        score_avg += i / max(score) * 100
    score_avg = score_avg / len(score)
print(score_avg)
# https://programmers.co.kr/learn/courses/30/lessons/87946
#  LV_2. 피로도


from itertools import permutations

def solution(k, dungeons):
    answer = -1
    per_dungeons = list(permutations(dungeons))
    for dungeon in per_dungeons:
        cnt = 0
        p = k
        for d in dungeon:
            if p >= d[0]:
                p -= d[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer


if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))
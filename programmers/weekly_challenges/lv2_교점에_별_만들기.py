# https://programmers.co.kr/learn/courses/30/lessons/87377
# LV2. 교점에 별 만들기


def solution(line):
    answer = []
    star = []
    x_max = y_max = -10**15
    x_min = y_min = 10**15
    for a in range(len(line)-1):
        for b in range(a+1, len(line)):
            cx = line[a][1]*line[b][2] - line[a][2]*line[b][1]
            cy = line[a][2]*line[b][0] - line[a][0]*line[b][2]
            cz = line[a][0]*line[b][1] - line[a][1]*line[b][0]
            if cz:
                if not (cx%cz or cy%cz):
                    x, y = cx//cz, cy//cz
                    x_max, y_max = max(x_max, x), max(y_max, y)
                    x_min, y_min = min(x_min, x), min(y_min, y)
                    star.append((x, y))
    star_map = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for s in star:
        star_map[y_max-s[1]][s[0]-x_min] = '*'
    for s_map in star_map:
        answer.append(''.join(s_map))
    return answer


if __name__ == '__main__':
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    print(solution(line))
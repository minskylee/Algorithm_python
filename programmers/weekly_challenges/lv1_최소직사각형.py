# https://programmers.co.kr/learn/courses/30/lessons/86491
# LV1. 최소직사각형


def solution(sizes):
    answer = 0
    a = b = 0
    for size in sizes:
        size.sort()
        a = max(a, size[0])
        b = max(b, size[1])
    answer = a*b
    return answer


if __name__ == '__main__':
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
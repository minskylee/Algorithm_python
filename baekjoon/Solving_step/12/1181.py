# https://www.acmicpc.net/problem/1181
# 단어 정렬


N = int(input())
word = []
for _ in range(N):
    word.append(input())
word = list(set(word))
word.sort()
word.sort(key= len)
print(*word, sep='\n')
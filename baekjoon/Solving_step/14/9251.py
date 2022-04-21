# https://www.acmicpc.net/problem/9251
# LCS


a = input()
b = input()
len_a, len_b = len(a), len(b)
lcs = [[0]*(len_b+1) for _ in range(len_a+1)]
for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])

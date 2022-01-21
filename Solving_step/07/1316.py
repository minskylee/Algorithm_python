T = int(input())

cnt = 0
for _ in range(T):
    voca = input()
    # 연속된 단어를 체크한다
    cont_voc = ''
    voc_cnt = 0
    for c in voca:
        if cont_voc == c:
            voc_cnt += 1
        cont_voc = c
    if len(set(voca)) == len(voca) - voc_cnt:
        cnt += 1
print(cnt)

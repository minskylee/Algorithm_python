# https://www.acmicpc.net/problem/17140
# 이차원 배열과 연산


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
while cnt <= 100:
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        break
    if len(arr) >= len(arr[0]): # R 연산
        max_len = 0
        arr_dta = []
        for i in range(len(arr)):
            cnt_dic = {}
            for j in range(len(arr[0])):
                if arr[i][j]:
                    if arr[i][j] not in cnt_dic:
                        cnt_dic[arr[i][j]] = 0
                    cnt_dic[arr[i][j]] += 1
            dta = []
            for ii in cnt_dic:
                dta.append((ii, cnt_dic[ii]))
            dta.sort(key= lambda x: (x[1], x[0]))
            arr_dta.append(dta)
            max_len = max(max_len, len(dta)*2)
        n_arr = [[0]*max_len for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr_dta[i])):
                n_arr[i][(j*2):(j*2)+2] = arr_dta[i][j]
    else:   # C 연산
        max_len = 0
        arr_dta = []
        for j in range(len(arr[0])):
            cnt_dic = {}
            for i in range(len(arr)):
                if arr[i][j]:
                    if arr[i][j] not in cnt_dic:
                        cnt_dic[arr[i][j]] = 0
                    cnt_dic[arr[i][j]] += 1
            dta = []
            for ii in cnt_dic:
                dta.append((ii, cnt_dic[ii]))
            dta.sort(key= lambda x: (x[1], x[0]))
            arr_dta.append(dta)
            max_len = max(max_len, len(dta)*2)
        n_arr = [[0]*len(arr[0]) for _ in range(max_len)]
        for j in range(len(arr[0])):
            for i in range(len(arr_dta[j])):
                n_arr[i*2][j] = arr_dta[j][i][0]
                n_arr[i*2+1][j] = arr_dta[j][i][1]
    if max_len > 100:
        arr = []
        if len(arr) >= len(arr[0]): # R 연산
            for i in range(len(arr)):
                arr.append(n_arr[i][:100])
        else:
            for j in range(100):
                arr.append(n_arr[j])
    else:
        arr = n_arr
    cnt += 1
print(-1 if cnt == 101 else cnt)

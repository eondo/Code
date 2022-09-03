# 2578. 빙고

# time :
# idea :
## 빙고판의 범위가 정해져 있으니까 빙고가 될 수 있는 모든 경우를 다 탐색하고 검사하면 됨

bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))
num_order = 0

for o in range(len(call)):
    num_order += 1# 한 번 불렀으니까 번째 + 1
    b_cnt = 0

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == call[o]:
                bingo[i][j] = 0

    # 행 합 검사
    for i in range(5):
        if sum(bingo[i]) == 0:
            b_cnt += 1

    # 열 합 검사
    for j in range(5):
        sum_col = 0
        for i in range(5):
            sum_col += bingo[i][j]

        if sum_col == 0:
            b_cnt += 1

    # 대각선 합 검사
    sum_d = 0
    sum_d_r = 0

    for l in range(5):
        sum_d += bingo[l][l]
        sum_d_r += bingo[4 - l][l]

    if sum_d == 0:
        b_cnt += 1
    if sum_d_r == 0:
        b_cnt += 1

    # 이제 빙고 개수는 다 세었고, 3개 이상 도달했는지 확인
    if b_cnt >= 3:
        print(num_order)
        break

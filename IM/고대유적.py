t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_l = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max_l:
                    max_l = cnt
            else:
                cnt = 0

    for j in range(m):
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max_l:
                    max_l = cnt
            else:
                cnt = 0

    # 만약 대각선으로도 1 연속된 게 있다면?
    for i in range(n):
        for j in range(m):
            cnt = 0
            ni = i
            nj = j

            while 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 1:
                cnt += 1
                ni += 1
                nj += 1

            if cnt > max_l:
                max_l = cnt


    print(f'#{tc} {max_l}')





    # for i in range(n):
    #     for j in range(m):
    #         cnt_j = 0
    #         cnt_i = 0
    #
    #         if arr[i][j] == 1:
    #             cnt_i += 1
    #             cnt_i += 1
    #             # 오른쪽 방향
    #             while arr[i][j + 1] == 1:
    #                 cnt_j += 1
    #                 j += 1
    #
    #             # 아래 방향
    #             while arr[i + 1][j] == 1:
    #                 cnt_i += 1
    #                 i += 1



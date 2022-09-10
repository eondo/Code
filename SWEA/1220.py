# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

# time :
# idea :
'''
1은 아래로 이동하고, 2는 위로 이동한다
근데 걱정되는 건 한번에 다 가야 하는데 하나마다 탐색해서 하는 게 아니라... 한꺼번에 한 턴에
어떻게 구현할까?
이동하는데 어디까지 이동하냐면 다음 그 칸이 0일때까지만 이동
그렇게 해서 각 열마다 / 교착 경우가 합이 3이니까 3으로 나눈 몫하면 개수
-> 수정 : 돌면서 현재 칸이랑 그 밑같 비교해서 다르면 cnt += 1
근데 몇 케이스는 정답보다 +1 만 차이남 어떤 예외가 존재한단 것 같은데 문제 발견 못 함
'''

# # 테케 10개 중 6개 통과
# for tc in range(1, 11):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 0

#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 1:
#                 if i + 1 < 0 or i + 1 >= n: # 범위 밖이면 0으로 만들고
#                     arr[i][j] = 0
#                 elif arr[i + 1][j] == 0: # 다음칸이 0이면 이동해서 지금 현재 위치는 0, 다음 위치는 자기값으로 바꿈
#                     arr[i][j] = 0
#                     arr[i + 1][j] = 1

#             elif arr[i][j] == 2:
#                 if i - 1 < 0 or i - 1 >= n:
#                     arr[i][j] = 0
#                 elif arr[i - 1][j] == 0:
#                     arr[i][j] = 0
#                     arr[i - 1][j] = 2

#     for i in range(n):
#         for j in range(n):
#             if 0 <= i + 1 < n:
#                 if (arr[i][j] == 1 and arr[i + 1][j] == 2) or (arr[i][j] == 2 and arr[i + 1][j] == 1):
#                     cnt += 1
#                     arr[i][j], arr[i + 1][j] = 0, 0


#     # for j in range(n):
#     #     col_sum = 0
#     #     for i in range(n):
#     #         col_sum += arr[i][j]
#     #
#     #     cnt += col_sum // 3

#     print(f'#{tc} {cnt}')


    # 구현 방법 수정 후 오답 Fail
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    
    breaker2 = False

    while breaker2 == False:
        new_arr = [[0] * n for _ in range(n)]
        breaker = False
        
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 1:
                    if i + 1 < 0 or i + 1 >= n: # 범위 밖이면 0으로 만들고
                        pass
                    elif arr[i + 1][j] == 0: # 다음칸이 0이면 이동해서 지금 현재 위치는 0, 다음 위치는 자기값으로 바꿈
                        new_arr[i][j] = 0
                        new_arr[i + 1][j] = 1
                    elif arr[i + 1][j] != 0:
                        new_arr[i][j] = 1

                elif arr[i][j] == 2:
                    if i - 1 < 0 or i - 1 >= n:
                        pass
                    elif arr[i - 1][j] == 0:
                        new_arr[i][j] = 0
                        new_arr[i - 1][j] = 2
                    elif arr[i - 1][j] != 0:
                        new_arr[i][j] = 2

        for i in range(n):
            if breaker == True:
                break
            for j in range(n):
                if 0 <= i + 1 < n:
                    if (new_arr[i][j] == 1 and new_arr[i + 1][j] == 0) or (new_arr[i][j] == 2 and new_arr[i - 1][j] == 0):
                        arr = new_arr # 바뀐 얘로 바꿔서 반영해주고 다음 턴!
                        breaker = True
                        
        else:
            # breaker2 = True
            break

    for k in range(n):
        for l in range(n):
            if 0 <= k + 1 < n:
                if (new_arr[k][l] == 1 and new_arr[k + 1][l] == 2) or (new_arr[k][l] == 2 and new_arr[k + 1][l] == 1):
                    cnt += 1
                    new_arr[k][l], new_arr[k + 1][l] = 0, 0


    # for j in range(n):
    #     col_sum = 0
    #     for i in range(n):
    #         col_sum += arr[i][j]
    #
    #     cnt += col_sum // 3

    print(f'#{tc} {cnt}')
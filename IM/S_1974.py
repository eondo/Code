# 1974. 스도쿠 검증
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&

# time : 15m
# idea :
## 특정 영역에 1 ~ 9까지 중복 없이 있다는 의미 -> 해당 영역을 다 더한 값이 딱 45여야 함
## 처음엔 셋을 써서 셋의 length가 9임을 확인하려고 했는데
## 그럼 계속 set.add()를 해줘야 하므로 set이 생성되니까 그냥 합이 더 용이할 것이라 생각
## 가로, 세로, 3x3칸마다 그 합이 45인지 체크하고 만약 45가 아닌 게 하나라도 발견되면 break
## 맞으면 1, 틀리면 0
# review :
## 1,2,3의 경우마다 하나라도 45 아닌 게 나오면 break 해주는데, 제대로 break가 안 걸리는 것 같음
## 답은 맞게 나오지만 필요 없는 연산을 계속 진행하게 되는 문제
## break문을 적절히 이용할 수 있는 법을 더 공부하여야 함 -> 현재 break를 준 곳마다 braker 변수 이용
## break 대신 breaker = True로 주고, for문마다 if breaker == True: -> break 조건을 줌


t = int(input())
for tc in range(1, t + 1):
    board = [list(map(int, input().split())) for _ in range(9)]#스도쿠 보드
    is_right = 1

    # 1. 모든 행의 합 검사
    for i in range(9):
        if sum(board[i]) != 45:
            is_right = 0
            break

    # 2. 모든 열의 합 검사
    for j in range(9):
        col_sum = 0
        for i in range(9):
            col_sum += board[i][j]

        if col_sum != 45:
            is_right = 0
            break

    # 3. 3x3 칸 합 검사

    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            block_sum = 0
            for i in range(3):
                for j in range(3):
                    block_sum += board[k + i][l + j]

            if block_sum != 45:
                is_right = 0
                break

    print(f'#{tc} {is_right}')


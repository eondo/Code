# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

t = int(input())

for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for i in range(100)]
    ladder_x = 99
    for where in range(100):
        if arr[99][where] == 2:
            ladder_y = where
            
    while ladder_x > 0:
        if ladder_y - 1 >= 0 and arr[ladder_x][ladder_y - 1] == 1:
            ladder_y -= 1
            while ladder_y - 1 >= 0 and arr[ladder_x][ladder_y - 1] == 1:
                ladder_y -= 1
            ladder_x -= 1

        elif ladder_y + 1 <= 99 and arr[ladder_x][ladder_y + 1] == 1:
            ladder_y += 1
            while ladder_y + 1 <= 99 and arr[ladder_x][ladder_y + 1] == 1:
                ladder_y += 1
            ladder_x -= 1

        else:
            ladder_x -= 1


    print(f'#{tc} {ladder_y}')
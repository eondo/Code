# 2116. 주사위 쌓기

# 주사위 숫자들이 주어지는데 ABCDEF 면이 정해져있으니까 인덱스 순서가 중요하겠다
# 0-5 인덱스, 1-3인덱스, 2-4인덱스 짝!

# 한 줄마다 아랫면인 거 정하고 그거의 짝인 인덱스의 값을 확인하고
# 그 밑 줄 주사위에서 해당 값에 해당하는 값 인덱스 찾고, 또 그거랑 짝은 인덱스 값 확인
# 또 그 값에 해당하는 인덱스 찾고,...
# 이 과정에서 찾는 그 값 (한 줄마다 2개씩)은 리스트에서 제외하고
# 남은 리스트에서 최대 값들을 모아 더한다

import copy # 1번 주사위의 밑면이 0~5 인덱스일 수 있기 때문에 깊은 복사해와서 계속 쓰자
num = int(input())

first_dice = [list(map(int, input().split())) for _ in range(num)] # 초기 주사위 정보 2차원 리스트

# 인덱스 짝을 어떻게 선언할까?
index_pair = [5, 3, 4, 1, 2, 0] 
# 구하고자 하는 최종 output 선언
max_side = 0 # 최대 옆면 합

for case in range(6):                       # 1번 주사위의 밑면 인덱스 값으로 어떤 것? (0~5인덱스 모두 가능하니까 반복문)
    dice = copy.deepcopy(first_dice)        # 밑 for문으로 리스트 원소가 제거되니까 케이스마다 dice 초기화
    
    for row in range(num):                  # 1번 주사위 ~ n번 주사위까지 윗밑면에 해당하는 값 제거
        if row == 0: # 1번 주사위
            down = dice[row][case]
            up = dice[row][index_pair[case]]
            dice[row].remove(down)
            dice[row].remove(up)
        else: # 나머지 주사위는 자기 윗줄 주사위에서 구해준 up, down에 영향을 받아서 처리
            down = dice[row][dice[row].index(up)]
            up = dice[row][index_pair[dice[row].index(up)]]
            dice[row].remove(down)
            dice[row].remove(up)

    sum_side = 0 # 제거 후 남은 리스트 들 중 각 주사위마다 최대값 구해서 더함
    for line in dice:
        sum_side += max(line)

    # 각 case마다 구한 옆면 합으로 max 업데이트
    if sum_side > max_side:
        max_side = sum_side

print(max_side)
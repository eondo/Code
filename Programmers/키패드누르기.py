# 키패드 누르기

## ✍️ 풀기 전 주석 작성
'''
1. 함수를 만들어서 if num(치고자하는 숫자)가

1) 1, 4, 7 중 하나면 answer += 'L' 해주고, 왼쪽 위치(lh) 업데이트

2) 3, 6, 9 중 하나면 answer += 'R' 해주고, 오른쪽 위치(rh) 업데이트

3) 그 나머지 2, 5, 8, 0 이면? 그때 들어온 lh와 숫자, rh와 숫자 거리 비교

1. 그럼 결국 numbers 리스트를 돌면서 lh, rh 변수는 그 전 거에서 영향을 받으니까
다음 numbers 인덱스로 넘어가도 이전 인덱스에서 어떤 처리를 하고 난 후의
lh, rh 변수값을 알고 있어야 함 -> 변수를 global로 주자
2. 그럼 특정 숫자와 lh, rh간의 거리를 알기 위해 사용해야 하는 건?
    1. 델타이동은 for문으로 무작위로 도니까 최소값을 찾지 않을 확률 높아보임
    2. 거리 계산은 이차원리스트에서 dfs로 하고, min_dis를 찾게 함
    근데 그럼 숫자의 (x, y)좌표값은 어떻게 알까? 그냥 매번 순회를 해야하는 것?
3. numbers를 돌면서 그냥 if elif else로 해주려고 했는데 이러면 그 전의
변수값 영향을 어떻게 받게 해주지? dfs로 재귀로? 근데 dfs는 아닐 것 같은 이유 : 
내가 하나의 number마다 선택할 수 있는 경우가 다양한 게 아니고 너무 명확하기 때문

💡
1. dfs보다 더 쉬운 풀이는 없을지 고민하기
2. 이차원리스트는 항상 주어진 것을 받아오는 게 아니라, 내가 입맛에 맞게 작성할 수 있음
    1. 이 경우 거리를 구하는 것에 대한 문제도 해결 가능!
'''

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
    
    
def solution(numbers, hand):
    answer = ''
    lh = [3, 0] 
    rh = [3, 2]
    
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            
        elif number in [3, 6, 9]:
            answer += 'R'
            
        elif number in [2, 5, 8, 0]:
            lh_dis = distance(lh, keypad[number])
            rh_dis = distance(rh, keypad[number])
            
            if lh_dis < rh_dis:
                answer += 'L'

            elif rh_dis < lh_dis:
                answer += 'R'

            else:
                if hand == 'left':
                    answer += 'L'

                else:
                    answer += 'R'

        if answer[-1] == 'L':
            lh = keypad[number]
        else:
            rh = keypad[number]
            
    # print(answer)
    return answer

keypad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

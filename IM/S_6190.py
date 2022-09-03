# 6190. 정곤이의 단조 증가하는 수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4

# time : 35m
# idea :
## 양의 정수 N개에서 나올 수 있는 모든 곱셈값들을 모두 구하고
## 그 곱셈값을 저장해둔 리스트에서 하나씩 꺼내서 해당 값이 단조증가인지 판별
## 단조증가의 경우, 현재까지의 max값과 비교했을 때 더 크다면 해당 값을 max로, 그렇지 않으면 버림
# review :
## for-else를 아직 자유자재로 쓸 수 있는 만큼의 역량을 갖추지 못한 것 같음
## 곱셈수들이 모두 단조증가가 아닌 경우는 괜찮은데, 곱셈수 리스트 마지막에 단조증가가 아니라고 해도 그 전까지의 max를 출력해야 하는 부분에서 실수
## 마지막 수가 단조증가가 아니면 마지막 수를 반영해 그대로 max가 -1로 출력되는 실수
## 이런 경우의 문제에는 기본값을 처음부터 -1으로 주고, 단조증가 조건을 통과하는 애들에 한해서 max 업데이트하도록 하자

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))# N개의 정수를 받아올 때 어떤 형식이 효율적인가, n이 매번 달라지니까 리스트 이용

    #이제 numbers에서 하나씩 꺼내어 값을 곱하고, 그 값을 곱셈한 값에 저장한다
    multi_num = []
    for i in range(n):
        for j in range(i + 1, n):
            multi_num.append(numbers[i] * numbers[j])

    #이제 곱셈값 리스트에서 하나의 원소마다 이게 단조증가인지 판별하고, max를 업데이트 한다
    max_num = -1

    for num in range(len(multi_num)):
        str_num = list(str(multi_num[num]))
        # 1. 얘를 분해
        for k in range(len(str_num)):#여기에 str_num이 몇 개의 자릿수로 이뤄져있는지 알아야 하는데
            if k + 1 < len(str_num) and int(str_num[k]) > int(str_num[k + 1]):# 2. 분해한 값 하나씩 접근하면서 다음 숫자보다 지금 숫자가 크면 탈락
                break

                # 이걸 왜 넣었던 거지?
                # if max_num <= -1:#이때까지 거쳐온 곱셈값이 다 단조증가 아니었으면 max가 -1이었을 거니까
                #     max_num = -1#근데 이번 곱셈값이 단조증가 아니더라도 전에 값이 있었으면 그걸로 써야 하니까
                # break

        else:# 3. 끝까지 탈락 안 됐으면 이제 max인지 확인
            if multi_num[num] > max_num:
                max_num = multi_num[num]

    print(f'#{tc} {max_num}')
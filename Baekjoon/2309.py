# 백준_2309. 일곱 난쟁이

# time : 50m
# idea :
## i, j인덱스를 pop해줄 때, i인덱스 제거하고 인덱스가 바뀌어서 pop을 주기에 곤란함
## 제외할 인덱스 i,j를 고르고 현재 리스트를 돌면서 i,j를 빼면서 더하는 과정을 삼중for문으로 구현

dwarf = [int(input()) for _ in range(9)]
breaker = False

for i in range(len(dwarf) - 1):
    if breaker == True:
        break

    for j in range(i + 1, len(dwarf)):
        sum_height = 0
        who = []

        for k in range(len(dwarf)):
            if k != i and k != j:
                sum_height += dwarf[k]
                who.append(dwarf[k])

        if sum_height == 100:
            breaker = True
            break

answer = sorted(who)

for one in answer:
    print(one)
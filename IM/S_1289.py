# 1289. 원재의 메모리 복구하기

# time :
# idea :
## 목표 메모리 값이랑 현재 메모리 값이랑 비교하면서 같은 index의 값들을 조작해주자

t = int(input())

for tc in range(1, t + 1):
    memory = list(input())
    now = ['0'] * len(memory)
    cnt = 0

    for i in range(len(now)):
        if now[i] != memory[i]:
            for j in range(i, len(now)):
                now[j] = memory[i]
            cnt += 1

    print(cnt)
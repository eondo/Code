# 1945. 간단한 소인수분해
# 리스트의 모든 원소들을 한 줄에 print할 때 언패킹을 쓰는데, f-string 쓸 때에 {}안에서는 * 쓸 수 없음

t = int(input())
n = [2, 3, 5, 7, 11]

for tc in range(1, t + 1):
    number = int(input())
    divide_cnts = [0] * len(n)

    for i in range(len(n)):
        divide_cnt = 0

        while number % n[i] == 0:
            divide_cnt += 1
            number = number / n[i]
        
        divide_cnts[i] = divide_cnt

    print(f'#{tc}', end=' ')
    print(*divide_cnts)


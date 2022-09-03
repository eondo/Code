# 6485. 삼성시의 버스 노선

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    ab_list = [0] * n

    for i in range(n):
        ab = list(map(int, input().split()))
        ab_list[i] = ab


    p = int(input())
    c_list = [0] * p

    for j in range(p):
        c_list[j] = int(input())

    result = [0] * p

    for c in range(len(c_list)):
        for ab in range(len(ab_list)):
            if ab_list[ab][0] <= c_list[c] <= ab_list[ab][1]:
                result[c] += 1

    print(f'#{tc}', end=' ')
    print(*result)

    
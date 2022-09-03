# 12712. 파리퇴치3

# time :
# idea :

t = int(input())

di1 = [0, 1, 0, -1] # 우하좌상
dj1 = [1, 0, -1, 0] # 우하좌상

di2 = [-1, 1, 1, -1] # 오위, 오아, 좌아, 좌위
dj2 = [1, 1, -1, -1]

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0

    for i in range(n):
        for j in range(n):
            sum_fly = arr[i][j]

            for k in range(4):
                for z in range(1, m):
                    ni1 = i + di1[k] * z
                    nj1 = j + dj1[k] * z

                    if 0 <= ni1 < n and 0 <= nj1 < n:
                        sum_fly += arr[ni1][nj1]


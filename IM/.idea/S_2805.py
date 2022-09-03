# 2805. 농작물 수확하기

# time :
# idea :
## i 인덱스가 달라지면서 해당 가로줄에서 접근하는 j 인덱스가 달라짐
## 무작위로 달라지지 않고 점점 늘려가거나, 줄어드는 방식
## 결국 n의 길이로 한정되어있는 곳에서 늘어났다가 줄어드는 방식임
## j의 인덱스의 범위가 range(a, b)라고 했을 때 a + b  = n (밭의 크기)임을 발견
# review :
## i가 달라지면서 j이 값이 달라질 때에는, j가 i가 뭔지에 따라 영향을 받고 있으니까
## j를 설정해주는 곳에 i가 붙은 range 식이 나옴

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    farm = [list(input()) for _ in range(n)]# 농작물 밭
    mid = n // 2# 중간값

    profit = 0

    for i in range(n):
        if i <= mid:# i가 0부터 중간값까지
            for j in range(mid - i, mid + i + 1):
                profit += int(farm[i][j])

        else:# i가 중간값 이후부터 끝까지
            for j in range(i - mid, n - (i - mid)):
                profit += int(farm[i][j])

    print(f'#{tc} {profit}')



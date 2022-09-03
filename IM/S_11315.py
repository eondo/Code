# 11315. 오목 판정

# time : 1h
# idea :
## 돌이 5개 이상 연속해야 yes라고 하면, 일단 최소 5개만 달성해도 yes니까 탐색하는 부분은 5개까지만 해도 된다
## 돌이 5개 연속 -> 돌 5개의 범위 안에서 돌 아닌 게 없다는 것과 같다
## 5개의 범위에서 돌 아닌 게 등장하면 break하고 다음 칸을 탐색하면 된다
## 이차원리스트로 받는 게 익숙하다고 생각이 드는데 그냥 문자열로 이뤄진 오목판으로도 풀 수 있지 않을까?
# review :
## 평소에 풀던 방법과 다른 방식을 생각하는 게 어려움
## 하나의 풀이법이 아니라 다양한 풀이법이 있을 수 있으니 다양한 접근법을 시도해보기
## 어떤 한 칸에서 연속되는 칸들을 모두 접근하고 어떤 조건에 부합 여부를 확인할 때 for-else 요긴히 쓸 수 있음
## 어떤 조건에 하나만 보고 끝이 아니라, 특정 범위를 다 싹 돌아보고, 여기에 걸리는 게 없을 때 어떤 처리를 해줄때

t = int(input())

for tc in range(1, t + 1):
    n = int(input())# 오목줄의 개수
    omok = [input() for _ in range(n)]
    is_omok = 'NO'
    breaker = False

    # 이제 모든 칸마다 접근해서 그 다음~다음 칸들이 .으로 끊기는지 검사

    for i in range(n):
        if breaker == True:
            break

        for j in range(n):

            # 아래
            if i + 4 < n:
                for k in range(5):
                    if omok[i + k][j] == '.':
                        break
                else:
                    is_omok = 'YES'
                    breaker = True

            if breaker == True:
                break

            # 오른쪽
            if j + 4 < n:
                for k in range(5):
                    if omok[i][j + k] == '.':
                        break
                else:
                    is_omok = 'YES'
                    breaker = True

            if breaker == True:
                break

            # \대각선
            if i + 4 < n and j + 4 < n:
                for l in range(5):
                    if omok[i + l][j + l] == '.':
                        break
                else:
                    is_omok = 'YES'
                    breaker = True

            if breaker == True:
                break

            # /대각선
            if i - 4 >= 0 and j + 4 < n:
                for l in range(5):
                    if omok[i - l][j + l] == '.':
                        break
                else:
                    is_omok = 'YES'
                    breaker = True

            if breaker == True:
                break

    print(f'#{tc} {is_omok}')


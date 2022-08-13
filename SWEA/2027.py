# 2027. 대각선 출력하기
# 이차원 리스트를 활용하여 배열의 대각선에 접근 및 할당

diagonal = list(['+'] * 5 for _ in range(5))

for i in range(len(diagonal)):
        diagonal[i][i] = '#'
        print(*diagonal[i], sep='')
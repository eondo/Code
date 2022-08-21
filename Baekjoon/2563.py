# 2563. 색종이
## 이차원 리스트의 접근

board = [[0] * 100 for _ in range(100)] # 도화지 : 0으로 채워진 100x100 이차원 리스트

num = int(input()) # 색종이 개수

cnt = 0 # 검은색 부분 칸의 수

for paper in range(num):
    a, b = map(int, input().split()) # a : 왼쪽 여백, b : 아래 여백
    
    # 색종이 범위 접근
    for i in range(100 - b - 10, 100 - b): # 색종이의 변이 10, 아래 여백 b를 반영
        for j in range(a, a + 10): # 왼쪽 여백 a부터 시작 -> a + 변 길이 10으로 끝
            
            # 색종이 범위를 1로 칠하고 카운팅
            if board[i][j] == 0: # 색종이가 겹쳐진 부분이라 이미 1로 채워진 경우 카운팅하지 않으므로 if 조건문
                board[i][j] = 1
                cnt += 1

print(cnt)
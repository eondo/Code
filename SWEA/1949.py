# 1949. [모의 SW 역량테스트] 등산로 조성
# time :
# idea
'''
가장 높은 봉우리에서 시작해야 하니까 시작점들은 정해져 있는 거구만
델타이동으로 현재 값보다 낮은 거라면 그 쪽으로 이동해서 쭉 가보면서 몇번 cnt 되는지 확인해야겠네
딱 한 곳 정해서 최대 k 깊이만큼 깎을 수 있다는 거 -> 1. 어디 칸을 선택? 2.
'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, cnt):
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < y and arr[x][y] > arr[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False

    # while arr[x][y] - arr[nx][ny] > 0:  # 동안 계속 확인한다
    print(cnt)


t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    max_height = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_height:
                dfs(i, j, 1)
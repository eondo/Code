# 1211. Ladder2

# time :
# idea
'''
이동거리가 같으면 가장 큰 x좌표 반환해야 하니까 오른쪽부터 검사하자
하좌우 이동일 필요하니까 델타 이동
하나의 출발점에서 도착점까지의 루트가 굉장히 많음 dfs로 풀어야 할까?
지금까지의 dfs는 1을 타고 가면서 그 수를 셌는데 이번에는 그렇게 풀면 안됨
그럼 하좌우만 움직이도록 제한을 두고, 거기서 가지치기로 좀 쳐내면 더 좋지 않을까
이전에 수업 시간에 언급됐던 미로 문제를 참고해보자
궁금한 것 : 나는 타고타고 가다가 여기서 안 되겠다 싶으면 되돌아왔으면 좋겠는데,
1) 여기까지만 돌아와! 라고 어느 지점까지만 되돌아오게 할 수 있는지,
2) 또 어디까지 되돌아오는 게 최적인지 뭘로 알 수 있으며, 3) 그걸 알 거나 구현하는 게 가능한 것인지
'''


def dfs(x, y):
    global cnt
    global min_cnt

    if cnt > min_cnt:
        return

    visited[x][y] = True    # 일단 여기로 들어왔다! 방문 처리 해주고
    cnt += 1    # 한 칸 왔으니까 cnt + 1
    # 이제 움직여야 하는데 어디로 움직일 것인가를 생각해보자
    # 델타 이동해야해!
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and not visited[nx][ny]:
            # 근데 만약에 여기가 마지막 행이면? 끝내줘야 하는데?
            if nx == 99:    # 99행이면 도착했단 거니까
                if cnt < min_cnt:   # min_cnt 업데이트해주고 끝
                    min_cnt = cnt
                return
            dfs(nx, ny) # 아직 안 끝났으면 가게 한다 쭉
            
            # now, 이상한 길로 갔으면 걔를 끊어주고 다시 이상한 길로 접어든 그 시점으로 되돌아오게 해주고 싶음



dx = [1, 0, 0]
dy = [0, -1, 1]

for _ in range(1, 2):
    tc = int(input())
    cnt = 0
    min_cnt = 10000

    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]   # 방문리스트

    for s in range(99, -1, -1):
        if ladder[0][s] == 1:   # 0행에서 i번째 열의 칸 값이 1이면 거기서 출발 가능!
            dfs(0, s)   # 여기서부터 함수 실행

    print(min_cnt)
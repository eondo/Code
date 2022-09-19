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
--0919수정--
생각해보니 위에서 고려한 가다가 잘못된 길일 경우 돌아오는 경우를 구현할 필요가 없었다.
해당 사다리는 가로 방향으로 나있는 1이면 그냥 쭉 가므로 델타값의 순서를 '하'가 마지막에 위치하게 두면 해결됨
'''
import copy


def dfs(x, y):
    global cnt
    global min_cnt
    global min_pos

    if cnt > min_cnt:           # 가지치기 (벌써 현재 min_cnt를 넘은 경로의 경우, cnt 세기 중단)
        return

    new_visited[x][y] = True    # 여기로 들어왔다는 방문 처리 해주고
    cnt += 1                    # 한 칸 왔으니까 cnt + 1 처리
    
    # 좌,우,하 순서로 그 칸에 접근할 수 있는지 for문으로 확인하고 접근
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and not new_visited[nx][ny]:
            # 만약 마지막 행이면 끝내줘야 함
            if nx == 99:    # 99행이면 도착했단 거니까
                if cnt < min_cnt:   # min_cnt 업데이트해주고 끝
                    min_cnt = cnt
                    min_pos = s
                return
            dfs(nx, ny) # 아직 안 끝났으면 해당 새로운 칸에서 쭉 가게 함


dx = [0, 0, 1]
dy = [-1, 1, 0]

for _ in range(1, 11):
    tc = int(input())
    min_cnt = 10000
    min_pos = 99

    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]   # 방문리스트

    for s in range(99, -1, -1):
        new_visited = copy.deepcopy(visited)    # 각 출발점마다 방문리스트 초기화
        if ladder[0][s] == 1:   # 0행에서 s번째 열의 칸 값이 1이면 거기서 출발 가능!
            cnt = 0
            dfs(0, s)   # 여기서부터 함수 실행

    print(f'#{tc} {min_pos}')
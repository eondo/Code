dx = [0, 1, 0, -1]  #우하좌상
dy = [1, 0, -1, 0]


def dfs(idx, cnt_core, cnt_line):
    global max_cnt_core
    global min_cnt_lines
    # 여기 들어와서 해줘야 할 것
    # 종료 조건 네!
    if idx == len(core):
        if cnt_core > max_cnt_core:
            max_cnt_core = cnt_core
            min_cnt_lines = cnt_line

        if cnt_core == max_cnt_core:
            if cnt_line < min_cnt_lines:
                min_cnt_lines = cnt_line
        return

    x, y = core[idx]    # 현재 위치 얘로 하겠다

    for k in range(4):  # 그리고 현재 위치에서 네 방향을 확인한다(이게 빠져야 하는지 고민)
        nx = x + dx[k]
        ny = y + dy[k]

        can_line = []

        while 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0 and not visited[nx][ny]:
                can_line.append((nx, ny))
                nx += dx[k]
                ny += dy[k]
                continue
            else:   # 위로 못 들어갔으면 이 방향은 불가능
                can_line = []   # 안에 든 거 없애주고
                break           # 멈추고 다른 방향을 보게 해줘야 함

        if can_line:
            for i in range(len(can_line)):
                li, lj = can_line[i]
                visited[li][lj] = True

            dfs(idx + 1, cnt_core + 1, cnt_line + len(can_line))
            for i in range(len(can_line)):  # 되돌려주기
                li, lj = can_line[i]
                visited[li][lj] = False

    dfs(idx + 1, cnt_core, cnt_line)


    # nx = x + dx[k]
    # ny = y + dy[k]
    #
    # can_line = []
    #
    # while 0 <= nx < n and 0 <= ny < n:
    #     if arr[nx][ny] == 0 and not visited[nx][ny]:
    #         can_line.append((nx, ny))
    #         nx += dx[k]
    #         ny += dy[k]
    #         continue
    #     else:  # 위로 못 들어갔으면 이 방향은 불가능
    #         can_line = []  # 안에 든 거 없애주고
    #         return  # 멈추고 다른 방향을 보게 해줘야 하는데?
    #
    #
    # for i in range(len(can_line)):
    #     li, lj = can_line[i]
    #     visited[li][lj]
    #
    #     # 다음 노드의 경우 보러 가기
    # for k in range(4):
    #     dfs(idx + 1, cnt_core + 1, cnt_line + len(can_line))



t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    core = []
    arr = []

    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(n):
            if row[c] == 1 and not (r == 0 or r == n - 1 or c == 0 or c == n - 1):
                core.append((r, c))
        arr.append(row)

    visited = [[False] * n for _ in range(n)]

    # 지금 내가 연결 판단하고 있는 코어 주인공 인덱스
    # 현재까지 연결된 코어 개수
    # 현재까지 연결된 전선 개수

    max_cnt_core = 0
    min_cnt_lines = n * n

    dfs(0, 0, 0)
    print(f'#{tc} {min_cnt_lines}')
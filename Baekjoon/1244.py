# 1233. 스위치 켜고 끄기

n = int(input()) # 스위치 개수
switch = list(map(int, input().split())) # 처음 스위치 상태를 담은 리스트
num = int(input()) # 스위치 상태를 바꿀 학생 수

for _ in range(num): # 한 번 학생이 들어올 때마다 스위치 상태를 바꿔주는 작업을 한다
    gender, number = map(int, input().split()) # 학생 성별, 학생이 받은 스위치 넘버

    # 1) 남학생일 때
    if gender == 1:
        for i in range(n): # 스위치 개수만큼 돌면서 스위치 상태 인덱스에 접근
            if (i + 1) % number == 0: # 인덱스 + 1이 넘버의 배수면
                switch[i] = (switch[i] + 1) % 2 # 상태 다음 칸으로 바꿔준다


    # 2) 여학생일 때
    else:
        switch[(number - 1)] = (switch[(number - 1)] + 1) % 2
        j = 1  # 일단 정의해주고 # (number - 1) 이게 지금 현재 번호칸의 인덱스

        while (number - 1) - j >= 0 and (number - 1) + j <= 7 and switch[(number - 1) - j] == switch[(number - 1) + j]:

            switch[(number - 1) - j] = (switch[(number - 1) - j] + 1) % 2
            switch[(number - 1) + j] = (switch[(number - 1) + j] + 1) % 2

            j += 1
        # 해당 스위치 넘버의 대칭을 찾아야 하는데 현재칸을 중심으로 만들어질 수 있는 줄 개수를 구하자
        # 만들어질 수 있는 줄 개수만큼 for문 반복으로 대칭을 확인하자
        # 생길 수 있는 줄 개수(대칭인지 확인할 반복 횟수) -> n - number 또는 number - 1
        # 즉, 현재 칸에서 왼쪽 남은 칸 개수, 오른쪽에 남은 칸 개수
        # 둘 중 작은 값을 대칭인지 확인할 반복 횟수를 정하자

        # 1. 반복할 횟수(현재칸 중심으로 만들어지는 줄 개수) 구하기
        if n - switch_number <= switch_number - 1:
            line_num = n - switch_number
        else:
            line_num = switch_number - 1
        # 2. 해당 반복수만큼 돌면서 왼쪽, 오른쪽 대칭 확인하기
        for j in range(1, line_num + 1): # 만들어지는 줄 다 구해서 반복하려고 했는데
            if switch[(switch_number - 1) - j:(switch_number - 1) + (j + 1)] == switch[(switch_number - 1) - j:(switch_number - 1) + (j + 1)][::-1]: # 대칭이면
                ?? 여기서 막힘
            # 점점 늘려가면서 회문인지 확인할 건데 조건에서 주어진 제일 긴 회문인 걸 어떻게 알지? -> 문제 발견 : 최대 길이의 회문을 찾고 난 후에 거기서 바꿔줘야 함

# 스위치 완성했고
print(switch)
# 이제 20개씩 끊어서 출력해주자
for i, v in enumerate(switch):
    if i != 0 and i % 20 == 0:
        print()
        print(v, end=' ')
    else:
        print(v, end=' ')
# while switch:
#     print(*switch[:20])
#     switch = switch[20:]
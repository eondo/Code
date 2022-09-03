# 5789. 현주의 상자 바꾸기

t = int(input())

for tc in range(1, t + 1):
    num_box, num_change = map(int, input().split())
    # 초기 상자 숫자
    box = [0] * num_box

    for i in range(num_change):
        l, r = map(int, input().split())

        for j in range(l, r + 1):
            box[j] += 1

    print(f'#{tc}', end=' ')
    print(*box)
    
    
     

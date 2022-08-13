# 1948. 날짜 계산기

t = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, t + 1):
    start_m, start_d, end_m, end_d = map(int, input().split())
    result = 0
    
    if start_m == end_m:
        result = end_d - start_d + 1
    
    else:
        result += days[start_m - 1] - start_d + end_d + 1

        for i in range(12):
            if start_m < i + 1 < end_m:
                result += days[i]
    print(f'#{tc} {result}')
        
            


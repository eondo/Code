# 2559. 수열

# time : 30m
# idea :
## n개 중에서 k개씩 묶으면서 이동하는 for문을 써야겠다
## 시간초과로 인하여 다른 방법인 슬라이싱 윈도우 사용

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

# # s1. 이중 for문 - 시간초과 남
# for i in range(n - k + 1):
#     sum_t = 0
#     for j in range(k):
#         sum_t += temperature[i + j]
#     if sum_t > max_t:
#         max_t = sum_t

# # s2. 슬라이싱 이용 - 시간초과
# for i in range(n - k + 1):
#     sum_t = sum(temperature[i:i+k])
#     if sum_t > max_t:
#         max_t = sum_t

# s3. 슬라이싱 윈도우
sum_first = sum(temperature[:k])#처음 연속된 온도의 sum 구하고
max_t = sum_first#걔를 초기 max로 지정

for i in range(1, n - k + 1):#슬라이싱 윈도우가 몇 번 쓰여야 하나
    sum_t = sum_first - temperature[i - 1] + temperature[i + (k - 1)]# 앞에 거 빼고, 뒤에 거 더하고
    if sum_t > max_t:
        max_t = sum_t
    sum_first = sum_t#sum_first 업데이트

print(max_t)
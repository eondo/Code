# 2491. 수열

# time :
# idea :
## 연속된 숫자가 계속 증가 혹은 감소하는지 보면서 그게 몇번 지속되고 있는지 count 해야 함
## 그리고 그렇게 count되는 게 끊길 수도 있고, 쭉 지속될 수도 있는데
## 그 중 가장 긴 count를 출력해야 하니까
## 순서가 중요하니까 함부로 정렬하면 안되겠고
## 한 숫자씩 옮길 때마다 커졌다, 작아졌다를 줘서 매번 초기화되기 전에 숫자 어디까지 찍었는지 볼까

n = int(input())
numbers = list(map(int, input().split()))

# 각 숫자 하나마다 단조 증가, 단조 감소의 경우 두 가지를 다 확인해봐야하나?
max_i = 0
max_d = 0
increasing = 1
decreasing = 1

for i in range(n):

    # # 이게 여기 들어가 있으면 자꾸 최댓값이 2로 나와서 밖으로 빼줬는데, 완벽하게 이해 x
    # increasing = 1
    # decreasing = 1

    if i + 1 < n and numbers[i] <= numbers[i + 1]:
        increasing += 1
    else:
        increasing = 1#로 초기화

    if i + 1 < n and numbers[i] >= numbers[i + 1]:
        decreasing += 1
    else:
        decreasing = 1

    # 한 숫자마다 만들어지는 i,d 마다 최댓값 갱신
    if increasing > max_i:
        max_i = increasing

    if decreasing > max_d:
        max_d = decreasing

print(max(max_i, max_d))
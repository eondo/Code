# 2635. 수 이어가기

# time :
# idea :
##

num = int(input())
max_cnt = 0
max_i = -1
cnt = 0


def count_max(x):
    global cnt
    if num - x < 0:
        return cnt
    else:
        cnt += 1
        return count_max(x) - count_max(num - x)


for i in range(num + 1):
    count_max(i)

    if count_max(i) > max_cnt:
        max_cnt = count_max(i)
        max_i = i

    # while num - i >= 0:
    #     a = b
    #     b = a - b
    #     cnt += 1
    # if cnt > max_cnt:
    #     max_cnt = cnt
    #     max_i = i

print(max_cnt, max_i)
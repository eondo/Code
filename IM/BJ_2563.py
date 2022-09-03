# 2563. 색종이

# time :
# idea :
##

paper = [[0] * 100 for _ in range(100)]

n = int(input())
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                cnt += 1
print(cnt)
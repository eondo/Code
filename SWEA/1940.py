# 가랏! RC카!

# 현재 속도를 쌓아야 함
mode = [0]
a = [0]
    
for i in range(int(input())):
    list_line = input().split()

    if len(list_line) == 2:
        m, v = map(int, list_line)
        mode.append(m)
        a.append(v)
    else:
        mode.append(0)
        a.append(0)

velocity = [0]

for status in range(1, len(mode)):

    if mode[status] == 1:
        velocity.append(velocity[status - 1] + a[status])


    elif mode[status] == 2:
        if velocity[status - 1] - a[status] <= 0:
            velocity.append(0)
        else:
            velocity.append(velocity[status - 1] - a[status])

    else:
        velocity.append(velocity[status - 1]) 

print(sum(velocity))
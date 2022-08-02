# 1대1 가위바위보

# 1
A, B = map(int, input().split())

if A > B:
    if A == 3 and B == 1:
        print('B')
    else:
	    print('A')
else:
    if A == 1 and B == 3:
        print('A')
    else:
        print('B')

# 2
A, B = map(int, input().split())

if 1 in {A, B} and 3 in {A, B}:
    if A > B:
        print('B')
    else:
        print('A')
else:
    if A > B:
        print('A')
    else:
        print('B')
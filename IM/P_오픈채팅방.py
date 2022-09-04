# 2019 KAKAO BLIND RECRUITMENT. 오픈채팅방

# time : 40m
# idea :

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
mode_list = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
id_nickname = dict()

# 1. 유저아이디-닉네임 연결한 딕셔너리 만들기
for i in range(len(record)):
    if 'Enter' in record[i] or 'Change' in record[i]:
        mode, userid, nickname = record[i].split()
        id_nickname[userid] = nickname

# 2. record의 모드에 따라 입력 받을 인자 수 나누고 딕셔너리에서 프린트할 값 매칭
for i in range(len(record)):
    if 'Leave' in record[i]:
        mode, userid = record[i].split()
        answer.append(f'{id_nickname[userid]}님이 {mode_list[mode]}')

    elif 'Enter' in record[i]:
        mode, userid, nickname = record[i].split()
        answer.append(f'{id_nickname[userid]}님이 {mode_list[mode]}')

print(answer)
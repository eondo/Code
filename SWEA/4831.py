# SWEA_4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

t = int(input())
for tc in range(1, t + 1):
    # avail_move : 한 번 충전 후 최대 갈 수 있는 양, num_station : 총 정류장 수, num_charge : 총 충전수 수
    avail_move, num_station, num_charge = map(int, input().split())
    # charge : 충전소 위치 리스트
    charge = list(map(int, input().split()))
    
    # fuel : 현재 버스가 갈 수 있는 정류장 수
    fuel = avail_move
    # charge_cnt : 충전 횟수
    charge_cnt = 0

    # 한 칸씩 버스를 움직이면서 fuel을 -1함
    for i in range(1, num_station):
        fuel -= 1
        # charge_stations : 현재 i에서 앞으로 남은 충전소들 리스트
        charge_stations = []
        
        # charge 리스트에서 현재 i보다 큰 수만 앞으로 갈 수 있는 충전소 리스트에 저장
        for charge_s in charge:
            if charge_s > i:
                charge_stations.append(charge_s)

        # 앞으로 충전소가 없어서 더 이상 충전할 수 없으면
        if not charge_stations: 
            # 현재 i에 충전소가 있고, fuel이 종점까지 가는데 부족한 경우
            # -> 충전
            if  i in charge and fuel < num_station - i:
                fuel = avail_move 
                charge_cnt += 1
                continue
            # 현재 i에 충전소가 업서고, fuel이 종점까지 가는데 부족한 경우
            # -> 도착 불가능, break
            elif fuel < num_station - i:
                charge_cnt = 0
                break
        
        # 나중에 갈 수 있는 충전소가 있다면
        else:
            # 다음 충전소까지 가는데 fuel이 부족한 경우
            if fuel - (min(charge_stations) - i) < 0:
                # 현재 충전소에서 충전
                if i in charge:
                    fuel = avail_move
                    charge_cnt += 1
                # 현재 충전소가 없다면 -> 도착 불가능
                else:
                    charge_cnt = 0
                    break
       
            # 다음 충전소까지 가는데 fuel이 충분하여 굳이 충전할 필요 없는 경우 -> 다음 i로 이동        
    print(f'#{tc} {charge_cnt}')

# 가능한 다른 풀이 Idea : while문으로 최대 갈 수 있는 만큼 갔을 때 그 중 오른쪽에서 가장 가까운 충전소에서 count
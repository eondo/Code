t = int(input())
for tc in range(1, t + 1):
    avail_move, num_station, num_charge = map(int, input().split())
    charge = list(map(int, input().split()))

    fuel = 3
    charge_cnt = 0

    for i in range(1, num_station):
        fuel -= 1
        if (fuel < 0) or (fuel == 0 and i not in charge):
            print(f'#{tc} {0}')
            break

        charge_stations = []
        for charge_s in charge:
            if charge_s > i:
                charge_stations.append(charge_s)
        # next_charge_s = min(charge_stations)
        # print(i, min(charge_stations))
        if not charge_stations: # 앞으로 충전소가 없어서 더 이상 충전할 수 없으면
            if i in charge and fuel == 0:
                fuel += avail_move
                charge_cnt += 1
                continue
            else:
                continue
        if fuel - (min(charge_stations) - i) < 0:
            if i in charge:
                fuel += avail_move
                charge_cnt += 1
            else:
                print(f'#{tc} {0}')
                break

    print(f'#{tc} {charge_cnt}')
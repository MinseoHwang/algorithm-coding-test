#입력
City_n = int(input())       #도시 개수
Road_d = list(map(int, input().split())) # 도로 거리
Oil_cost = list(map(int, input().split()))   # 도시 별 ㄴ기름 값

Total_cost = 0

for i in range(City_n-1):
    if Oil_cost[i] >= Oil_cost[i+1]:
        Total_cost += (Oil_cost[i] * Road_d[i])
    else:
        Total_cost += (Oil_cost[i] * (Road_d[i]+Road_d[i+1]))
        break

print(Total_cost)
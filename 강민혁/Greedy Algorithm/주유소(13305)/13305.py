#입력
City_n = int(input())       #도시 개수
Road_d = list(map(int, input().split())) # 도로 거리
Oil_cost = list(map(int, input().split()))   # 도시 별 ㄴ기름 값

Total_cost = 0      # 총 기름 가격

best = Oil_cost[0]  # 기준 설정

for i in range(City_n-1):
    if best > Oil_cost[i]:  # 현재 최저 기름값보다 Oil_cost[i] 값이 더 작을 경우 기준을 변경해서 최소 기름값을 구하게 한다.
        best = Oil_cost[i]
    Total_cost += (best * Road_d[i])

print(Total_cost)
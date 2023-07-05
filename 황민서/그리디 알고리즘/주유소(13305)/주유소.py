# 처음 시작은 무조건 거리 리스트의 첫번째 요소 * 기름 리스트의 첫번째 요소이다.
# 처음 가격을 default 값으로 하여 도시를 지나면서 현재 도시가 기름 값이 더 싸다면 현재 도시의 기름값을 선택하는 식으로 풀면 될 것이다

#입력
N = int(input())
distance = list(map(int, input().split()))
fuel = list(map(int, input().split()))

#구현
result = 0

min_price = fuel[0]
for i in range(N-1):
    if min_price > fuel[i]:
        min_price = fuel[i]
    result += min_price * distance[i]

#출력
print(result)
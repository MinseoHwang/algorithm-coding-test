import sys
input = sys.stdin.readline # 빠른 입력을 위해 sys.stdin.readline을 사용
n = int(input()) # 사용자로부터 도로의 개수를 입력받음

length = list(map(int, input().split()))  # 도로의 길이들을 공백으로 구분하여 입력받고 리스트로 변환
price = list(map(int, input().split())) # 주유소의 가격들을 공백으로 구분하여 입력받고 리스트로 변환


result = 0 # 최종 비용을 저장할 변수 초기화
fuel = price[0]  # 현재까지의 최소 주유소 가격을 저장하는 변수 초기화
for i in range(n-1): # 모든 도로에 대해 반복하여 최소 비용 계산
    if fuel > price[i]: # 현재 도로의 주유소 가격이 이전까지의 최소 주유소 가격보다 작다면 최소 주유소 가격을 갱신
        fuel = price[i] 
    result += fuel * length[i]  # 현재 도로의 길이에 현재까지의 최소 주유소 가격을 곱하여 최소 비용에 더함
print(result) # 최소 비용 출력

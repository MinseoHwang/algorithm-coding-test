import sys

coins = []
count = 0

c_coin, total = map(int, input().split(" ")) # 동전의 종류 개수와 동전의 합을 입력 받는다.

for i in range(c_coin):     # 동전의 종류를 배열로 입력 받는다.
    coins.append(int(sys.stdin.readline()))


# 동전을 최소로 사용하기 위해 큰 동전부터 사용해야 한다. # c_coins
coins.reverse() # 동전을 내림차순으로 정렬한다.

for coin in coins:
    count += total // coin # 사용한만큼의 동전의 개수를 기억한다.
    total %= coin   # 계산되고 남은 금액을 total에 저장한다.

print(count)

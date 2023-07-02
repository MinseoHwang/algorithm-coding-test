# 동전 0(11047번) 목표하는 금액인 K값보다 작은 동전 금액을 K값에서 빼주고 남은 금액에서 이 과정을 계속 반복하는 식으로 구현할 것임 


#입력
N, K = input().split() # N = 동전 종류 개수 K = 목표하는 금액
N = int(N)
K = int(K)
money = [] # 동전 종류
for i in range(0, N):
    a = int(input())
    money.append(a)


# 구현

remaining = 0 #남은 돈
cnt = 0 # 카운트
for i in reversed(range(0, N)): # reversed()는 리스트의 원소들을 거꾸로 뒤집고 이를 반환하는 함수
     while(money[i] <= K): # K보다 작은 동전을 골라서 목표 금액에 맞게 넣을 수 있을 만큼 넣음
          K = K - money[i]
          cnt += 1

# 출력
print(cnt)
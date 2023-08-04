import sys

input = sys.stdin.readline
N = int(input()) 
count = 0 #코인의 개수 초기화
coin_type = [500,100,50,10] #코인의 종류를 배열로 저장
for i in coin_type: 
    count += N // i 
    N  %= i 
print(count)
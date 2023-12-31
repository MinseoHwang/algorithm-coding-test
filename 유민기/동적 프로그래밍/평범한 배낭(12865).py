import sys

r = sys.stdin.readline
n, k = map(int, r().split())# 물품의 수 N과 가방의 용량 K 입력 받기
d = [0] * (k + 1)# 가치의 합을 저장할 리스트 초기화

# 가치의 합을 저장할 리스트 초기화
for _ in range(n):
    w, v = map(int, r().split())# 물건의 무게 W와 가치 V 입력 받기
    # 현재 가방의 용량부터 물건의 무게까지 역순으로 반복
    for i in range(k, w - 1, -1):
        d[i] = max(d[i - w] + v, d[i])# 이전에 구한 가치와 현재 물건의 가치를 비교하여 최댓값 저장
print(d[k])# 가방의 용량 K에서 얻을 수 있는 최대 가치 출력


"""
1. 입력을 받고 가치의 합을 저장할 리스트 d를 초기화한다.
2. 각 물건에 대해서 무게와 가치를 입력받고, 가방의 용량부터 해당 물건의 무게까지 역순으로 반복한다.
3. 현재 물건을 가방에 넣을 수 있는지를 확인하고, 넣을 수 있다면 이전에 구한 가치와 현재 물건의 가치를 비교하여 최댓값을 저장합니다.
4.모든 물건에 대한 반복이 끝나면, 가방의 용량 K에서 얻을 수 있는 최대 가치를 출력합니다.
"""

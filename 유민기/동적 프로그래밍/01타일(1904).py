import sys
input = sys.stdin.readline # 빠른 입력을 위해 sys.stdin.readline을 사용
n = int(input()) # 사용자로부터 정수 n을 입력받음

d = [0] * 1000001  # 크기가 1000001인 리스트 d를 생성하고 0으로 초기화
d[1] = 1  # d[1]은 1로 초기화 (2×1 크기의 직사각형을 채우는 방법은 1가지)
d[2] = 2  # d[2]는 2로 초기화 (2×2 크기의 직사각형을 채우는 방법은 2가지: 가로 2개 또는 세로 2개)

for k in range(3, n + 1): # 3부터 n까지 반복하여 d[k]를 계산
    d[k] = (d[k - 1] + d[k - 2]) % 15746  # d[k]는 d[k-1]과 d[k-2]를 더한 값으로 계산되며, 15746으로 나눈 나머지를 저장함.(overflow 방지)
print(d[n])  # 결과 출력: 2×n 크기의 직사각형을 채우는 방법의 수를 d[n]에 저장했으므로, d[n]을 출력합니다.

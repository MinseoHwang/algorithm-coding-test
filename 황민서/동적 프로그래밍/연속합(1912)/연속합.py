#연속되는 수열 중에서 합이 가장 큰 부분들의 합을 출력하는 문제이다
#bottom up 방식으로 문제를 접근하였다. 리스트의 첫 부분부터 시작하여 더해나가는데, 이전에 더한 값보다 현재 값이 크다면 현재 값을 dp리스트에 넣어주고 이를 반복한다.
# dp 리스트 안에 있는 숫자들 중 가장 큰 값이 바로 답이 될 것이다.

#입력 및 변수 설정
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (n+2)

#구현
dp[1] = arr[1]
for i in range(2, n+1):
    dp[i] = max(arr[i], dp[i-1]+ arr[i])

#출력
print(max(dp[1:n+1]))

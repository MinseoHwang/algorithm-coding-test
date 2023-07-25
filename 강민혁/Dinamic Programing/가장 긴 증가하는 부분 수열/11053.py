#배열 길이 입력
N = int(input())
#배열 입력
arr = list(map(int, input().split()))

#dp의 모든 인덱스값을 1로 초기화
dp = [1] * N

#Logic
# arr[j]와 arr[i]를 비교하여 arr[j] < arr[i]가 되면 dp[i]값은 증가한다.
# 계속해서 큰수를 읽을때마다 dp[i]값이 1씩 더해진다.
for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

#출력
#print(dp)
print(max(dp))
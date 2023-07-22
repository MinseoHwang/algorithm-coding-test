import sys
input = sys.stdin.readline

n = int(input())  

p = list(map(int, input().split()))

dp  = [1] * n

for i in range(1, n):
    for j in range(i):
        if p[i] > p[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

"""풀이:
1.n = 6, p = 10, 20, 10, 30, 20, 50을 입력 받는다
2. 입력받은 값 n을 dp에 배열로 저장한다. 
3. 변수 i가 (1 ~ n)구간을 반복한다.
4. 변수 j가 (1 ~ n)구간에서 반복한다.
5. p[i] > p[j]일 경우 dp[i]는 최댓값(dp[i], dp[j]+1)을 가진다.
6. 최댓값 dp를 출력한다.



조금더 직관적은 풀이
p = [10, 20 ,10, 30, 20 ,50] -> dp = [1,1,1,1,1,1]

1.  p1[i=1], p0[j=0]
    p[1] > p[0] : True 
    -> dp = [1,?,?,?,?,?]
2.  p2[i=2], p1[j=1], p0[j=0]
    p[2] > p[0] : False 
    p[2] > p[1] : False
    -> dp = [1,2,?,?,?,?]
3.  p3[i=1], p2[i=2], p1[i=1], p0[i=0]
    p[3] > p[0] : True
    p[3] > p[1] : False
    p[3] > p[2] : False
    -> dp = [1,2,1,?,?,?]
4.  p4[i=3], p3[i=1], p2[i=2], p1[i=1], p0[i=0]
    p[4] > p[0] : True
    p[4] > p[1] : True
    p[4] > p[2] : True
    p[4] > p[3] : True
    -> dp = [1,2,1,3,?,?]
5.  p5[i=2], p4[i=3], p3[i=1], p2[i=2], p1[i=1], p0[i=0]
    p[5] > p[0] : True
    p[5] > p[1] : False
    p[5] > p[2] : False
    p[5] > p[3] : False
    p[5] > p[4] : False
    -> dp = [1,2,1,3,1,?]
6.  p6[i=5], p5[i=2], p4[i=3], p3[i=1], p2[i=2], p1[i=1], p0[i=0]
    p[6] > p[0] : True
    p[6] > p[1] : True
    p[6] > p[2] : True
    p[6] > p[3] : True
    p[6] > p[4] : True
    p[6] > p[5] : True
    -> dp = [1,2,1,3,1,4]

위 결과로 dp의 최댓값이 4임을 알게되었다
그러므로 결과값 max(dp)를 출력한다
"""

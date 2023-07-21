import sys
input = sys.stdin.readline # 빠른 입력을 위해 sys.stdin.readline을 사용
n = int(input()) # 사용자로부터 정수 n을 입력받음

def fib(n):
    if n == 1 or n == 2:
        return 1   # n이 1이거나 2인 경우, 1을 반환
    else: 
        return (fib(n - 1) + fib(n - 2)) # n이 1 또는 2가 아닌 경우, 이전 두 항의 합을 반환
    
def fibonacci(n):
    f = [0] * (n+1)  # 길이가 n+1인 리스트 f를 생성하고 모든 요소를 0으로 초기화
    f[1], f[2] = 1,1  # 초기 조건: f[1]과 f[2]는 모두 1
    c = 0  # 카운터 변수 c를 0으로 초기화
    for i in range(3, n+1): # 3부터 n까지 반복
        c += 1 # 반복 횟수를 세기 위해 c를 1씩 증가
        f[i] = f[i - 1] + f[i - 2] 
    return c  # 카운터 변수 c를 반환


print(fib(n),fibonacci(n)) # fib(n)과 fibonacci(n)의 결과를 출력

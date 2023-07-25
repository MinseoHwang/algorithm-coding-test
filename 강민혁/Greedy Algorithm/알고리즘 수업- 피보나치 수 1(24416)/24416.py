# n의 피보나치 수를 재귀호출과 동적프로그래밍으로 구하는 알고리즘

# 입력
n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def fibonacci(n):
    f = [1, 1]
    i = 2
    count = 0
    for i in range(2, n-1):
        f.append(f[i-1] + f[i-2]) # 코드2
        i += 1
        count += 1      # While문에 한번 돌때마다 실행횟수를 1씩 증가시킨다.
    return count


#출력
print(fib(n), n-2)

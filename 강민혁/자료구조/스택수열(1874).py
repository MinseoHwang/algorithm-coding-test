n = input()
stack = []
result = []
cnt = 1

for i in range(n):
    num = int(input())
    while cnt <= num: # 입력받은 숫자가 cnt보다 작거나 같을 때
        stack.append(cnt)
        result.append("+")
        cnt += 1

    if stack[-1] == num:    # stack에 마지막 숫자와 num이 같을 때
        stack.pop()
        result.append("-")
    else:
        print("No")
        exit(0)

for i in result:
    print(i)

t = int(input())

for i in range(t):
    stack = []
    str = input()
    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:   # '(' 가 stack에 있지 않은데 ')'가 들어올 때
                print("No")
                break
    else:
        if not stack:
            print("Yes")
        else:
            print("No")
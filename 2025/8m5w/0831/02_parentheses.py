import sys
sys.stdin = open("parentheses_input.txt", "r")
sys.stdout = open("parentheses_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    texts = list(input())
    stack = []
    result = 1

    for text in texts:
        if text in "{(":
            stack.append(text)

        elif text in "})":
            if not stack:
                result = 0
                break
            
            if text == "}" and stack[-1] == "{":
                stack.pop()
            elif text == ")" and stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f"#{testcase} {result}")
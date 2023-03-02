class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            # print(stack)
            # print(tokens[i])
            if tokens[i].isdigit() or (len(tokens[i]) > 1 and tokens[i][0] == '-'):
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == "/":
                    temp = num2 / num1
                elif tokens[i] == '+':
                    temp = num2 + num1
                elif tokens[i] == '*':
                    temp = num2*num1
                else:
                    temp = num2 - num1
                stack.append(int(temp))
                # print(temp)
        return int(stack[-1])
                    
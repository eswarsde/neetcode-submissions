class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop() # right operand
                a = stack.pop() # left operand
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # // → floor division (rounds down toward negative infinity)
                    # int(a/b)- Truncation toward zero → discard decimal part (round toward zero)
                    stack.append((int(a/b)))
        return stack[0]


        
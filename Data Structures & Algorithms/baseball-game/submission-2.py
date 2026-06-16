class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
     
            if op == "+":
                 plus = stack[-1] + stack[-2]
                 stack.append(plus)
            elif op == "D":
                d = stack[-1]*2
                stack.append(d)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        
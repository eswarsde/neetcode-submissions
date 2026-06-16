class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # easy one
        result = [0] * len(temperatures)

        stack = [] # previously seen temp, index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_Temp, stack_Index = stack.pop()
                result[stack_Index] = i - stack_Index
            stack.append((temp,i))

        return result 
 
        
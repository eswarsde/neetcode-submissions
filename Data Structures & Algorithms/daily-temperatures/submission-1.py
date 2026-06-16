class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # easy understanding 
        result = [0] * len(temperatures)

        stack = [] # (previouslyseen_temp, index)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_Temp, stack_Index = stack.pop()
                result[stack_Index] = i - stack_Index
            stack.append((temp,i))
        return result 

        # better way is store only the index, since we can fetch the temp from temperatures array itself
        # for i, temp in enumerate(temperatures):

        #     while stack and temp > temperatures[stack[-1]]:
        #         stack_index  = stack.pop()
        #         result[stack_index] = i - stack_index
        #     stack.append(i)
        # return result
 
        
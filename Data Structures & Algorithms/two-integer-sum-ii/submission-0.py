class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                left+=1 # Return the indices (1-indexed) of two numbers,
                right+=1
                return [left, right]
            
            if current_sum < target:
                left+=1
            else:
                right-=1
        
        return [-1, -1]

        
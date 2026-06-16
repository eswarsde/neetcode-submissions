class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        

        num_to_string = str(x)
        num_length = len(num_to_string)

        if num_length == 1:
            return True
        
        left = 0
        right = num_length - 1

        while left < right:
            if num_to_string[left] != num_to_string[right]:
                return False
            left+=1
            right-=1
        return True
            
        
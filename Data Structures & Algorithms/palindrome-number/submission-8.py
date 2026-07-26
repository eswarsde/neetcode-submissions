class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reversed = 0
        # 101 % 10 = 1 (reminder)
        # 101 // 10 = 10 (quotient)
        # 10 % 10 = 0
        #  
    
        while x:
            digit = x % 10 
            reversed = reversed * 10 + digit
            x //= 10

        return original == reversed
        
    #     # Time complexity: O(n)
    #     # Space complexity: O(1)

 # 1221
 # reversed = 0
 # 1) 1221 % 10 => 1
 #  reversed = reversed*10 + 1

   


























    # # converting integer to string approach 

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     str_num = str(x)
    #     length = len(str_num)

    #     if length == 1:
    #         return True

    #     left = 0
    #     right = length -1
        
    #     while left < right:
    #         if str_num[left] != str_num[right]:
    #             return False
    #         left+=1
    #         right-=1
    #     return True 

    #     # Time complexity: O(n)
    #     # Space complexity: O(n)


        
  
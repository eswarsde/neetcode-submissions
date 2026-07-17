class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ""
        if len(s) <=1:
            return s

        def expand(left: int, right: int) -> str:
            # Walk outward while the pair matches and stays in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Pointers overshot by one, so pull back in
            return s[left + 1:right]


        for centre_postion in range(len(s)):
            odd = expand(centre_postion, centre_postion)
            even = expand(centre_postion, centre_postion+1)
            result = max(result, odd, even, key=len)

        return result
    
    # # brute force
    # def isPalindrome(self, text):

    #     left = 0
    #     right = len(text) - 1

    #     while left < right:
    #         if text[left] != text[right]:
    #             return False
    #         left+=1
    #         right-=1
    #     return True

    # def longestPalindrome(self, s: str) -> str:

    #     # brute force
    #     n = len(s)

    #     if n <= 1:
    #         return s

    #     # substrings of all length starting from longest to shortest
    #     for substring_length in range(n, 0, -1):
    #         for start in range(n - substring_length + 1):
    #             substring_candidate = s[start: start+substring_length]
    #             if self.isPalindrome(substring_candidate):
    #                 return substring_candidate
    #     return "" 
    #     # Time complexity: O(n^3)
    #     # space complexity: O(n)


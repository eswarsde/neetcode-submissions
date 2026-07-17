class Solution:

    def isPalindrome(self, text):

        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left+=1
            right-=1
        return True

    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        # substrings of all length starting from longest to shortest
        for substring_length in range(n, 0, -1):
            for start in range(n - substring_length + 1):
                substring_candidate = s[start: start+substring_length]
                if self.isPalindrome(substring_candidate):
                    return substring_candidate
        return ""        
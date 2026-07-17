class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack_len = len(haystack)
        needle_len = len(needle)

        result = 0

        if haystack_len < needle_len:
            return -1
        
        if haystack_len == needle_len and haystack == needle:
            return 0

        for i in range(0, haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i

        return - 1
        

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abcadefgh

        L = 0 
        R - expanding part of the window until range(len(n))
        dict = {} last seen char - this is to avoid repeating characters
             "a": 1

          [abc] <= a
            i    
        """
        left = 0
        last_seen = {} # char: index
        result = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1 # remove/ move the left pointer until bcomes valid
            
            last_seen[ch] = right # add to the lookup

            curr_length = right - left + 1

            result = max(result, curr_length)
        
        return result
class Solution:
    def helper(self, s, t):
        char_map = {}
        for i, char in enumerate(s):
            if char not in char_map:
                char_map[char] = t[i]
            if char in char_map and char_map[char] != t[i]:
                return False
        
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return self.helper(s, t) and self.helper(t, s)





        # does not work because it ignores position 

        # This code fails below case
        # s="bbbaaaba"
        # t="aaabbbba"

        # unique_char_s = set(s) 
        # unique_char_t = set(t)

        # if len(unique_char_s) ==  len(unique_char_t):
        #     return True
        # return False
        
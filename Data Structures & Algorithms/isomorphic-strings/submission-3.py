class Solution:
    #     Why we need two maps
    # Using only one map is not enough.

    # Example:
    # s = "ab"
    # t = "cc"
    # A one-way map could allow:

    # a -> c
    # b -> c
    # But that is invalid because two different characters cannot map to the same target.

    # So we maintain:

    # s_to_t[char_s] = char_t
    # t_to_s[char_t] = char_s
    # This guarantees a one-to-one mapping.

    def isIsomorphic(self, s: str, t: str) -> bool:

        # Isomorphic strings must match character-by-character by position,
        # so different lengths can never work.
        if len(s) != len(t):
            return False

        # Forward map: character in s -> character in t.
        s_to_t = {}

        # Reverse map: character in t -> character in s.
        # This prevents two different characters in s from mapping to one in t.
        t_to_s = {}

        # Traverse both strings once from left to right.
        for i in range(len(s)):
            # Current work at this position: compare this character pair.
            char_s = s[i]
            char_t = t[i]

            # If both characters are new, create a fresh two-way mapping.
            if char_s not in s_to_t and char_t not in t_to_s:
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s
                continue

            # Otherwise, the pair is only valid if both stored mappings agree.
            # dict.get(...) returns None for unseen characters, which correctly
            # fails the equality check if only one side was seen before.
            if s_to_t.get(char_s) != char_t or t_to_s.get(char_t) != char_s:
                # Edge case / conflict:
                # - char_s was mapped to a different target, or
                # - char_t was already claimed by a different source.
                return False

        # We finished the full scan without conflicts, so the mapping is valid.
        return True














    # def helper(self, s, t):
    #     char_map = {}
    #     for i, char in enumerate(s):
    #         if char not in char_map:
    #             char_map[char] = t[i]
    #         if char in char_map and char_map[char] != t[i]:
    #             return False
        
    #     return True

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     return self.helper(s, t) and self.helper(t, s)






















































        # does not work because it ignores position 

        # This code fails below case
        # s="bbbaaaba"
        # t="aaabbbba"

        # unique_char_s = set(s) 
        # unique_char_t = set(t)

        # if len(unique_char_s) ==  len(unique_char_t):
        #     return True
        # return False
        